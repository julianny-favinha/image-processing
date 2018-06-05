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

			p1 = (row_floor, col_floor)
			p2 = (row_floor, col_ceil)
			p3 = (row_ceil, col_floor)
			p4 = (row_ceil, col_ceil)

			img1 = img[p1[0]][p1[1]]
			img2 = img[p2[0]][p2[1]]
			img3 = img[p3[0]][p3[1]]
			img4 = img[p4[0]][p4[1]]

			dx = abs(row/dic["scale"] - round(row/dic["scale"]))
			dy = abs(col/dic["scale"] - round(col/dic["scale"]))

			new_img[row][col] = (1-dx)*(1-dy)*img1 + (dx)*(1-dy)*img2 + (1-dx)*(dy)*img3 + (dx)*(dy)*img4

	io.imsave(dic["outputname"], new_img)
