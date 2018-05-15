from skimage import color, data, exposure, feature, io, transform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

""" 
Algoritmo de detecção de inclinação baseada em transformada de Hough.

Input: imagem RGBA.
"""

"""
max_angle = angulo de maior frequencia em angles
"""
def objective(angles):
	# determina frequencia de cada angulo
	angles_dict = {}
	for angle in angles:
		if angle in angles_dict.keys():
			angles_dict[angle] += 1
		else:
			angles_dict[angle] = 1

	# encontra o angulo que possui o maior frequencia
	max_angle = np.rad2deg(max(angles_dict, key=angles_dict.get))

	# ajustando angulo para texto nao ficar de ponta cabeca
	if max_angle > 0:
		max_angle -= 90
	else:
		max_angle += 90

	return max_angle

def hough_transform(img, img_output_name):
	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)
	img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

	# deteccao de bordas
	edges = feature.canny(img_gray)

	# deteccao de linhas
	hspace, angles, dists = transform.hough_line(edges)
	hspace, angles, dists = transform.hough_line_peaks(hspace, angles, dists)

	# calcula angulo de maior frequencia
	max_angle = objective(angles)

	print("Angle = %d degrees" % (max_angle))

	# salva imagem rotacionada
	img_rotated = transform.rotate(img, max_angle, mode='edge', resize=True)
	io.imsave(img_output_name, img_rotated)
