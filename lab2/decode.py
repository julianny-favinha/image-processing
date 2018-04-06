import sys
from skimage import io

"""
python3 decode.py output.png

INPUT
- img_output.png: imagem com a mensagem embutida.

OUTPUT
- text.txt: mensagem que estava embutida na imagem.
- plane_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.
"""

# reads file image
file_name = sys.argv[1]
img_colored = io.imread(file_name)