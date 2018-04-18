import sys
import time
from skimage import io
import numpy as np

BITS = 8

# retorna o valor inteiro da string b, composta apenas por 0s e 1s
def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(BITS)[::-1])

# retorna o valor binário do inteiro d em uma string
def toDecimal(b):
	return int(b, 2)

# retorna a bit-ésima posição de string, de trás para frente 
def getBit(string, bit):
	return string[BITS - 1 - bit]


start_time = time.time()

# parametros de entrada
file_name, file_name_extension = sys.argv[1].split(".")
file_name_extension = "." + file_name_extension
bit_plane = int(sys.argv[2])

# le a imagem de entrada e cria as duas imagens dos planos de saida
img_colored = io.imread(file_name + file_name_extension)

# abre o arquivo texto para escrever a mensagem que será lida
f = open(file_name + "_text.txt", "w")
bits = ""
color = 0
write_file = True

"""Para cada canal de cor do pixel img_colored[linha][coluna],
	Concatena o bit da posicao bit_plane menos siginificativo na variavel bits
	Se o tamanho de bits chegou em 8, entao podemos ler um caractere da mensagem
	Salvar o caractere lido no arquivo texto de saida"""
for row in range(0, img_colored.shape[0]):
	for col in range(0, img_colored.shape[1]):
		for color in range(0, 3):
			pixel_rgb = img_colored[row][col]
			bit = getBit(toBinary(pixel_rgb[color]), bit_plane)
			bits = bits + bit

			if len(bits) == BITS:
				if write_file and toDecimal(bits) != 0:
					f.write(chr(toDecimal(bits)))			
					bits = ""
				else:
					write_file = False

# fecha o arquivo texto
f.write("\n")
f.close()

# calcula tempo decorrido
elapsed_time = time.time() - start_time
print("Elapsed time: %1f s" %(elapsed_time))
