import numpy as np
from skimage import io

def neighbor(img, row, col):
	row = int(round(row))
	if row >= img.shape[0] or row < 0:
		return 255

	col = int(round(col))
	if col >= img.shape[1] or col < 0:
		return 255

	return img[row][col]
