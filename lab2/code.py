import sys
from skimage import io

"""
python3 code.py input.png bit_plane text.txt

INPUT
- img_input.png: imagem onde sera embutida a mensagem.
- bit_plane: três planos de bits menos significativos, sendo 0, 1 ou 2
- text.txt: mensagem a ser oculta.

OUTPUT
- img_output.png: imagem com mensagem embutida.
- plane_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.
"""

RED = 0
GREEN = 1
BLUE = 2

def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(8)[::-1])

def toDecimal(b):
	return int(b, 2)

def substituteCharAt(string, char, position):
	#print("string %s, char %c, position %d" %(string, char, position))
	return string[:position] + char + string[(position+1):]

def save_plane(img_colored, file_name, bit_plane):
	f = open(file_name, "w+")
	for row in range(0, img_colored.shape[0]):
		for col in range(0, img_colored.shape[1]):
			f.write("%d " %(img_colored[row][col][bit_plane]))
		f.write("\n")

def readText(file_name):
	f = open(file_name, "r")
	return f.read().strip()

# params
file_name = sys.argv[1]
bit_plane = int(sys.argv[2])
file_text_name = sys.argv[3]

# reads file image and stores the 3 channels RED, GREEN and BLUE
img_colored = io.imread(file_name)
save_plane(img_colored, "plane_img_red", RED)
save_plane(img_colored, "plane_img_green", GREEN)
save_plane(img_colored, "plane_img_blue", BLUE)

with open(file_text_name) as file_text:
	row = 0
	col = 0
	while True:
		letter = file_text.read(1)
		if not letter or letter == "\n":
			break
		# transform c decimal ascii to binary
		letter_binary = toBinary(ord(letter))

		i = 0
		while i < len(letter_binary):
			""" pegar o valor  img_colored[x][y] -> array [R, G, B]
				transformar R para binario, trocar o bit 0 1 ou 2 menos significativo por c
				voltar R para decimal e colocar na imagem de saida"""
			# chegou ao final da linha
			if col == img_colored.shape[1]:
				row += 1
				col = 0

			pixelRgb = img_colored[row][col]
			img_colored[row][col][RED] = toDecimal(substituteCharAt(toBinary(pixelRgb[RED]), letter_binary[i], 7 - bit_plane))
			i += 1
			if i < len(letter_binary):
				img_colored[row][col][GREEN] = toDecimal(substituteCharAt(toBinary(pixelRgb[GREEN]), letter_binary[i], 7 - bit_plane))
				i += 1
				if i < len(letter_binary):
					img_colored[row][col][BLUE] = toDecimal(substituteCharAt(toBinary(pixelRgb[BLUE]), letter_binary[i], 7 - bit_plane))
					i += 1
					col += 1

save_plane(img_colored, "plane_new_red", RED)
save_plane(img_colored, "plane_new_green", GREEN)
save_plane(img_colored, "plane_new_blue", BLUE)

