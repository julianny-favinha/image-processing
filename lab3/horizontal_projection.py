from skimage import io, transform, exposure, color
import numpy as np

""" 
Algoritmo de detecção de inclinação baseada em projeção horizontal.

Input: imagem RGBA.
"""

"""
profile[i] = quantidade de pixels pretos da linha i
"""
# TODO: está com limiarização global
def calculate_profile(img):
	profile = np.zeros((img.shape[0]), dtype=int)
	
	for row in range(0, img.shape[0]):
		for col in range(0, img.shape[1]):
			if img[row][col] < 0.8:
				profile[row] += 1

	return profile

"""
value = soma dos quadrados das diferenças dos valores em células adjacentes do perfil de projeção
"""
def calculate_value(profile):
	value = 0

	for row in range(0, profile.shape[0]-1):
		value += (profile[row] - profile[row+1]) ** 2

	return value

def horizontal_projection(img, img_input_name):
	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)

	# TODO: mudar. está com limiariazação global
	img_gray[img_gray < 0.8] = 0.0

	# cria dicionario com key angulo e value valor da função objetivo 
	value = {}
	for angle in range(1, 181):
		value[angle] = 0 

	# calcula profile e value para a imagem rotacionada em angle
	for angle in value.keys():
		img_rotated = transform.rotate(img_gray, angle)
		profile_rotated = calculate_profile(img_rotated)
		value[angle] = calculate_value(profile_rotated)
	
	# encontra o angulo que possui o maior value
	max_angle = max(value, key=value.get)

	# imprime angulo na saida padrao 
	print("Angle %d degrees" % (max_angle))
	if max_angle > 90:
		max_angle -= 180

	# salva imagem rotacionada
	img_perfect = transform.rotate(img, max_angle)
	io.imsave(img_input_name.replace(".png", "") + "_horizontal_output.png", img_perfect)	
