from skimage import color, exposure, io, transform, util
import numpy as np

""" 
Algoritmo de detecção de inclinação baseada em projeção horizontal.

Input: imagem RGBA.
"""

"""
profile = quantidade de pixels pretos para cada linha
"""
def calculate_profile(img):
	return np.sum(img, axis=1)

"""
value = soma dos quadrados das diferenças dos valores em células adjacentes do perfil de projeção
"""
def calculate_value(profile):
	return np.sum(np.square(np.diff(profile)))

"""
max_ angle = angulo de maior frequencia em value
"""
def objective(value):
	max_angle = max(value, key=value.get)

	if max_angle > 90:
		max_angle -= 180

	return max_angle

def horizontal_projection(img, img_output_name):
	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)

	# binarizacao da imagem dado um limiar global
	img_gray[img_gray < 0.8] = 0.0
	img_gray[img_gray >= 0.8] = 1.0
	img_gray = util.invert(img_gray)

	# cria dicionario com key angulo e value valor da funcao objetivo 
	value = {}
	for angle in range(0, 181):
		value[angle] = 0 

	# calcula profile e value para a imagem rotacionada em angle
	for angle in value.keys():
		img_rotated = transform.rotate(img_gray, angle, resize=True)
		profile_rotated = calculate_profile(img_rotated)
		value[angle] = calculate_value(profile_rotated)
	
	# calcula angulo com maior frequencia
	max_angle = objective(value)
	print("Angle = %d degrees" % (max_angle))	

	# salva imagem rotacionada
	img_rotated = transform.rotate(img, max_angle, mode='edge', resize=True)
	io.imsave(img_output_name, img_rotated)
