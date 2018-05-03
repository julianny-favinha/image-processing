import sys
from skimage import io
from horizontal_projection import horizontal_projection
from hough_transform import hough_transform

"""
EXECUÇÃO DO PROGRAMA
python3 align.py imagem_entrada.png modo imagem_saida.png

modo E ['horizontal', 'hough']
"""

# parametros de entrada
img_input_name = sys.argv[1]
mode = sys.argv[2]
img_output_name = sys.argv[3]

# le a imagem de entrada
img = io.imread(img_input_name)

if mode == "horizontal":
	horizontal_projection(img)
else:
	hough_transform(img)
