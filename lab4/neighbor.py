import numpy as np
from skimage import io, exposure

def neighbor(dic):
	print("neighbor")

	# le a imagem de entrada
	img = io.imread(dic["inputname"])

	# dimensoes da nova imagem
	new_img = np.zeros(shape=(int(img.shape[0]*dic["scale"]), int(img.shape[1]*dic["scale"])), dtype=np.uint8)

	for row in range(0, new_img.shape[0]-1):
		for col in range(0, new_img.shape[1]-1):
			new_img[row][col] = img[round(row/dic["scale"])][round(col/dic["scale"])]

	io.imsave(dic["outputname"], new_img)
