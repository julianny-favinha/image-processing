import sys
import time
from skimage import io
import numpy as np

"""
python3 decode.py output.png plane_bits

INPUT
- img_output.png: imagem com a mensagem embutida.
- plane_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.

OUTPUT
- text_output.txt: mensagem que estava embutida na imagem.
- img_output_bit_planex.png: imagem do plano de bits x
"""

BITS = 8

def toDecimal(b):
	return int(b, 2)

def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(BITS)[::-1])

def getBit(string, bit):
	return string[BITS - 1 - bit]

start_time = time.time()

# parameters
file_name = sys.argv[1]
bit_plane = int(sys.argv[2])

# reads image
img_colored = io.imread(file_name)
img_bit_plane = np.array(img_colored, copy=True)
img_bit_plane7 = np.array(img_colored, copy=True)

# open file do write message hidden
f = open(file_name.replace("img_output.png", "") + "text_output.txt", "w")
bits = ""
color = 0
write_file = True

for row in range(0, img_colored.shape[0]):
	for col in range(0, img_colored.shape[1]):
		for color in range(0, 3):
			"""para cada canal do pixel de posicao [row][col], concatena o bit_plane menos significativo em bits
				se o tamanho de bits chegou em 8, entao podemos ler um char
				salva o char no arquivo texto de saida"""
			pixel_rgb = img_colored[row][col]
			bit = getBit(toBinary(pixel_rgb[color]), bit_plane)
			img_bit_plane[row][col][color] = int(bit)
			bits = bits + bit

			bit7 = getBit(toBinary(pixel_rgb[color]), BITS - 1)
			img_bit_plane7[row][col][color] = int(bit7)
	
			if len(bits) == BITS:
				if write_file and toDecimal(bits) != 0:
					f.write(chr(toDecimal(bits)))			
					bits = ""
				else:
					write_file = False

f.write("\n")
f.close()

img_bit_plane[img_bit_plane > 0] = pow(2, bit_plane)
img_bit_plane7[img_bit_plane7 > 0] = pow(2, BITS-1)

io.imsave(file_name.replace(".png", "") + "_bit_plane" + str(bit_plane) + ".png", img_bit_plane)
io.imsave(file_name.replace(".png", "") + "_bit_plane7.png", img_bit_plane7)

elapsed_time = time.time() - start_time
print("Elapsed time: %1f s" %(elapsed_time))
