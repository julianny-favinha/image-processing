import numpy as np
from skimage import io

def R(s):
	return (1/6)*(pow(P(s+2), 3) - 4*pow(P(s+1), 3) + 6*pow(P(s), 3) - 4*pow(P(s-1), 3))

def P(s):
	return s if s > 0 else 0

def bicubic(dic):
	print("bicubic")

	# le a imagem de entrada
	img = io.imread(dic["inputname"])

	# dimensoes da nova imagem
	new_img = np.zeros(shape=(int(img.shape[0]*dic["scale"]), int(img.shape[1]*dic["scale"])), dtype=np.uint8)

	for row in range(0, new_img.shape[0]-1):
		for col in range(0, new_img.shape[1]-1):
			dx = abs(row/dic["scale"] - round(row/dic["scale"]))
			dy = abs(col/dic["scale"] - round(col/dic["scale"]))

			value = 0.0

			for m in range(-1, 3):
				for n in range(-1, 3):
					img_row = round(row/dic["scale"]) + m 
					if img_row >= img.shape[0]:
						img_row = img.shape[0]-1
					elif img_row < 0:
						img_row = 0

					img_col = round(col/dic["scale"]) + n
					if img_col >= img.shape[1]:
						img_col = img.shape[1]-1
					elif img_col < 0:
						img_col = 0

					value += img[img_row][img_col]*R(m-dx)*R(dy-n)
		
			new_img[row][col] = round(value)
	io.imsave(dic["outputname"], new_img)
