from skimage import io, transform, exposure, color
import numpy as np

""" 
Algoritmo de detecção de inclinação baseada em projeção horizontal.
"""

"""
img[row][col] retorna array [a, b, c, d] entre 0 e 255, onde
	- (a, b, c) é são os canais RGB
	- d é o canal Alpha
"""

"""
profile[i] = quantidade de pixels pretos da linha i
"""
# TODO: está com limiarização global
def calculate_profile(img):
	profile = np.zeros((img.shape[0]), dtype=int)
	
	for row in range(0, img.shape[0]):
		for col in range(0, img.shape[1]):
			if img[row][col] < 200.0:
				profile[row] += 1

	return profile

def horizontal_projection(img, img_input_name):
	print("horizontal")
	
	# número de linhas e colunas da imagem	
	rows = img.shape[0]	
	cols = img.shape[1]
	
	# transformação para escala de cinza
	img_gray = color.rgb2gray(img)
	img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

	# TODO: mudar. está com limiariazação global
	img_gray[img_gray < 200] = 0

	# calcula perfil da imagem original
	profile_gray = calculate_profile(img_gray)

	"""
	value[angle] = soma dos quadrados das diferenças dos valores em células adjacentes do perfil de projeção
	"""
	value = {}
	for angle in range(0, 361):
		value[angle] = 0 

	for angle in value.keys():
		# rotaciona imagem em um angulo angle
		img_rotated = transform.rotate(img_gray, angle)

		# calcula perfil da imagem rotacionada
		profile_rotated = calculate_profile(img_rotated)
	
		for row in range(0, profile_rotated.shape[0]-1):
			value[angle] += (profile_rotated[row] - profile_rotated[row+1]) ** 2
	
	# encontra o ângulo que possui o maior value
	max_value = value[0]
	max_angle = 0	
	for angle in value.keys():
		if value[angle] > max_value:
			max_value = value[angle]
			max_angle = angle

	print("Ângulo %d" % (max_angle))

	# salva imagem rotacionada
	img_perfect = transform.rotate(img_gray, max_angle)
	img_perfect = exposure.rescale_intensity(img_perfect, out_range=(0, 1))
	io.imsave(img_input_name + "_horizontal_output.png", img_perfect)	
