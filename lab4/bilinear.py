import numpy as np
from math import ceil, floor
from skimage import io

def bilinear(dic):
	print("bilinear")

	# le a imagem de entrada
	img = io.imread(dic["inputname"])

	# dimensoes da nova imagem
	new_img = np.zeros(shape=(int(img.shape[0]*dic["scale"]), int(img.shape[1]*dic["scale"])), dtype=np.uint8)

	for row in range(0, new_img.shape[0]-1):
		for col in range(0, new_img.shape[1]-1):
			row_floor = floor(row/dic["scale"])
			row_ceil = ceil(row/dic["scale"]) if ceil(row/dic["scale"]) < img.shape[0] else img.shape[0]-1
			col_floor = floor(col/dic["scale"])
			col_ceil = ceil(col/dic["scale"]) if ceil(col/dic["scale"]) < img.shape[1] else img.shape[1]-1

			img1 = img[row_floor][col_floor]
			img2 = img[row_floor][col_ceil]
			img3 = img[row_ceil][col_floor]
			img4 = img[row_ceil][col_ceil]

			dx = abs(row/dic["scale"] - round(row/dic["scale"]))
			dy = abs(col/dic["scale"] - round(col/dic["scale"]))

			new_img[row][col] = (1-dx)*(1-dy)*img1 + (dx)*(1-dy)*img2 + (1-dx)*(dy)*img3 + (dx)*(dy)*img4

	io.imsave(dic["outputname"], new_img)
