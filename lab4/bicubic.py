import numpy as np
from skimage import io

def R(s):
	return (1/6)*(pow(P(s+2), 3) - 4*pow(P(s+1), 3) + 6*pow(P(s), 3) - 4*pow(P(s-1), 3))

def P(s):
	return s if s > 0 else 0

def bicubic(img, dic):
	print("bicubic")

	# scale in x and in y
	scale_x = dic["dimensions"][1] / img.shape[1]
	scale_y = dic["dimensions"][0] / img.shape[0]

	# dimensoes da nova imagem
	new_img = np.zeros(shape=(dic["dimensions"][1], dic["dimensions"][0]), dtype=np.uint8)

	for row in range(0, new_img.shape[0]):
		for col in range(0, new_img.shape[1]):
			dx = abs(row/scale_x - round(row/scale_x))
			dy = abs(col/scale_y - round(col/scale_y))

			value = 0.0

			for m in range(-1, 3):
				for n in range(-1, 3):
					img_row = round(row/scale_x) + m 
					if img_row >= img.shape[0]:
						img_row = img.shape[0]-1
					elif img_row < 0:
						img_row = 0

					img_col = round(col/scale_y) + n
					if img_col >= img.shape[1]:
						img_col = img.shape[1]-1
					elif img_col < 0:
						img_col = 0

					value += img[img_row][img_col]*R(m-dx)*R(dy-n)
		
			new_img[row][col] = round(value)
	io.imsave(dic["outputname"], new_img)
