import sys
from skimage import io

"""
python3 decode.py output.png plane_bits

INPUT
- img_output.png: imagem com a mensagem embutida.
- plane_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.

OUTPUT
- text_output.txt: mensagem que estava embutida na imagem.
"""

BITS = 8

def toDecimal(b):
	return int(b, 2)

def toBinary(d):
    return ''.join(str(1 & int(d) >> i) for i in range(BITS)[::-1])

def getBit(string, bit):
	return string[BITS - 1 - bit]

# parameters
file_name = sys.argv[1]
bit_plane = int(sys.argv[2])

# reads image
img_colored = io.imread(file_name)

# open file do write message hidden
f = open(file_name.replace("img_output.png", "") + "text_output.txt", "w")

bits = ""
color = 0
stop = False
for row in range(0, img_colored.shape[0]):
	for col in range(0, img_colored.shape[1]):
		for color in range(0, 3):
			"""para cada canal do pixel de posicao [row][col], concatena o bit_plane menos significativo em bits
				se o tamanho de bits chegou em 8, entao podemos ler um char
				salva o char no arquivo texto de saida"""
			pixel_rgb = img_colored[row][col]
			bits = bits + getBit(toBinary(pixel_rgb[color]), bit_plane)
	
			if len(bits) == 8:
				if toDecimal(bits) == 0:
					stop = True
					break

				f.write(chr(toDecimal(bits)))			
				bits = ""
		if stop:
			break
	if stop:
		break

f.close()
