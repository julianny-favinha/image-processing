import sys
from skimage import io

"""
python3 code.py input.png text.txt

INPUT
- img_input.png: imagem onde sera embutida a mensagem.
- text.txt: mensagem a ser oculta.

OUTPUT
- img_output.png: imagem com mensagem embutida.
- plane_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.
"""

# reads file image
file_name = sys.argv[1]
img_colored = io.imread(file_name)
print(img_colored)