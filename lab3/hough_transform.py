from skimage import color, data, exposure, feature, io, transform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

""" 
Algoritmo de detecção de inclinação baseada em transformada de Hough.

Input: imagem RGBA.
"""

def hough_transform(img, img_output_name):
	print("hough")

	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)
	img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

	# binarizacao da imagem dado um limiar global
	img_gray[img_gray < 200] = 0
	img_gray[img_gray >= 200] = 255

	# deteccao de bordas
	edges = feature.canny(img_gray)

	""" ALGORITMO DO PROFESSOR"""
	"""for row in range(0, img_gray.shape[0]):
		for col in range(0, img_gray.shape[1]):
			if img_gray[row][col] == 255:
				acumulador = hough(row, col)"""
				

	angles = {}
	# deteccao de linhas
	lines = transform.probabilistic_hough_line(edges, threshold=10, line_length=25, line_gap=3)
	#print(lines)

	for ((x1, y1), (x2, y2)) in lines:
		angle = (y2 - y1) / (x2 - x1)
		if angle in angles.keys():
			angles[angle] += 1
		else:
			angles[angle] = 1

	""" para cada linha em lines, detectar o angulo? arredondar para int.
		fazer tipo um dicionario de {angulo:frequencia} ???"""

	print(angles)

	# encontra o angulo que possui o maior value
	max_angle = max(angles, key=angles.get)
	print(max_angle)
	print("Angle = %d degrees" % (np.rad2deg(max_angle)))

	# salva imagem rotacionada
	img_rotated = transform.rotate(img, np.rad2deg(max_angle))
	io.imsave(img_output_name, img_rotated)	
