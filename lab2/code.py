import sys
from skimage import io

"""
python3 code.py input.png bit_plane text.txt

INPUT
- img_input.png: imagem onde sera embutida a mensagem.
- bit_plane: três planos de bits menos significativos, sendo 0, 1 ou 2
- text_input.txt: mensagem a ser oculta.

OUTPUT
- img_output.png: imagem com mensagem embutida.
*********************************************************************************************************************
"""

BITS = 8

def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(BITS)[::-1])

def toDecimal(b):
	return int(b, 2)

def substituteCharAt(string, char, position):
	return string[:position] + char + string[(position+1):]

def save_plane(img_colored, file_name, bit_plane):
	f = open(file_name, "w+")
	for row in range(0, img_colored.shape[0]):
		for col in range(0, img_colored.shape[1]):
			f.write("%d " %(img_colored[row][col][bit_plane]))
		f.write("\n")
	f.close()

def readText(file_name):
	f = open(file_name, "r")
	return f.read()[:-1]

# parameters
file_name = sys.argv[1]
bit_plane = int(sys.argv[2])
file_text_name = sys.argv[3]

# reads file image and stores the 3 channels RED, GREEN and BLUE
img_colored = io.imread(file_name)
save_plane(img_colored, "plane_img_red", 0)
save_plane(img_colored, "plane_img_green", 1)
save_plane(img_colored, "plane_img_blue", 2)

# \0 é a condição de parada para podermos decodificar posteriormente
message = readText(file_text_name) + "\0"

row = 0
col = 0
color = 0

binary_message = ""
for letter in message:
	binary_message += toBinary(ord(letter))

for bit in binary_message:
	# chegou ao final da linha
	if col == img_colored.shape[1]:
		row += 1
		col = 0

	""" valor R = img_colored[x][y] retorna um array [R, G, B]
		transformar R para binario, trocar o bit 0, 1 ou 2 menos significativo por c
		voltar valor novo para decimal e colocar na imagem de saida"""
	pixel_rgb = img_colored[row][col]
	img_colored[row][col][color] = toDecimal(substituteCharAt(toBinary(pixel_rgb[color]), bit, BITS - 1 - bit_plane))
	
	# passou por todas as cores de uma coluna
	if color + 1 == 3:
		col += 1

	color = (color + 1) % 3

save_plane(img_colored, "plane_new_red", 0)
save_plane(img_colored, "plane_new_green", 1)
save_plane(img_colored, "plane_new_blue", 2)
io.imsave(file_name.replace(".png", "") + "_output.png", img_colored)

