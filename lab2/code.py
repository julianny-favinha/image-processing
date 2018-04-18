import sys
import time
from skimage import io

BITS = 85
MAX_INTENSITY = 25

# retorna o valor inteiro da string b, composta apenas por 0s e 1s
def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(BITS)[::-1])

# retorna o valor binário do inteiro d em uma string
def toDecimal(b):
	return int(b, 2)

# substitui a posicao position de string pelo caractere char
def substituteCharAt(string, char, position):
	return string[:position] + char + string[(position+1):]

# le o texto de um arquivo
def readText(file_name):
	f = open(file_name, "r")
	return f.read()[:-1]


start_time = time.time()

# parametros de entrada
file_name, file_name_extension = sys.argv[1].split(".")
file_name_extension = "." + file_name_extension
bit_plane = int(sys.argv[2])
file_text_name = sys.argv[3]

# le a imagem de entrada
img_colored = io.imread(file_name + file_name_extension)
img_bit_plane = np.array(img_colored, copy=True)
img_bit_plane7 = np.array(img_colored, copy=True)

# le a mensagem a ser esteganografada na imagem e coloca o caractere \0 ao final, como critério de parada
message = readText(file_text_name) + "\0"

row = 0
col = 0
color = 0

# transforma cada caractere da imagem em sua representação binária
binary_message = ""
for letter in message:
	binary_message += toBinary(ord(letter))

# verifica se o texto cabe na imagem
if len(binary_message) > img_colored.size:
	print("Message is bigger than image. Consider input a smaller text or a bigger image.")
	sys.exit()

""" img_colored[linha][coluna] retorna um array [R, G, B].
	Seja P o valor de img_colored[linha][coluna][R].
	Transformar P para binario;
	Trocar o bit bit_plane menos significativo por bit;
	Voltar novo valor para decimal e inserir na imagem de saida"""
for bit in binary_message:
	# chegou ao final da linha
	if col == img_colored.shape[1]:
		row += 1
		col = 0

	# chegou ao final da imagem
	if row == img_colored.shape[0]:
		break

	pixel_rgb = img_colored[row][col]
	img_colored[row][col][color] = toDecimal(substituteCharAt(toBinary(pixel_rgb[color]), bit, BITS - 1 - bit_plane))
	
	# passou por todas as cores de um pixel
	if color + 1 == 3:
		col += 1

	color = (color + 1) % 3

for row in range(0, img_colored.shape[0]):
	for col in range(0, img_colored.shape[1]):
		for color in range(0, 3):
			bit = getBit(toBinary(pixel_rgb[color]), bit_plane)
			img_bit_plane[row][col][color] = int(bit)

			bit7 = getBit(toBinary(pixel_rgb[color]), BITS - 1)
			img_bit_plane7[row][col][color] = int(bit7)

# transformação de intensidade
# isso é feito para podermos visualizar melhor as imagens dos planos. caso contrário, elas ficariam escuras demais
img_bit_plane[img_bit_plane > 0] = MAX_INTENSITY
img_bit_plane7[img_bit_plane7 > 0] = MAX_INTENSITY

# salva as imagens
io.imsave(file_name + "_bit_plane" + str(bit_plane) + file_name_extension, img_bit_plane)
io.imsave(file_name + "_bit_plane7" + file_name_extension, img_bit_plane7)

# salva imagem de saida
io.imsave(file_name + "_output" + file_name_extension, img_colored)

# calcula tempo decorrido
elapsed_time = time.time() - start_time
print("Elapsed time: %1f s" %(elapsed_time))

