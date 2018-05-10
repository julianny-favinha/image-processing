from skimage import color, data, exposure, feature, io, transform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

""" 
Algoritmo de detecção de inclinação baseada em transformada de Hough.

Input: imagem RGBA.
"""

def hough_transform(img, img_output_name):
	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)
	img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

	# binarizacao da imagem dado um limiar global
	img_gray[img_gray < 200] = 0
	img_gray[img_gray >= 200] = 255

	# deteccao de bordas
	edges = feature.canny(img_gray)

	# deteccao de linhas
	lines = transform.probabilistic_hough_line(edges, threshold=10, line_length=25, line_gap=3)

	# determina frequencia de cada angulo
	angles = {}
	for ((x1, y1), (x2, y2)) in lines:
		if x2 - x1 != 0:
			angle = (y2 - y1) / (x2 - x1)
			if angle in angles.keys():
				angles[angle] += 1
			else:
				angles[angle] = 1

	# encontra o angulo que possui o maior frequencia
	max_angle = np.rad2deg(max(angles, key=angles.get))
	print("Angle = %d degrees" % (max_angle))

	# salva imagem rotacionada
	img_rotated = transform.rotate(img, max_angle, mode='edge')
	io.imsave(img_output_name, img_rotated)
