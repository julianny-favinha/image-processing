import numpy as np
from math import ceil, floor
from skimage import io

def boundary(img, row, col):
	if row >= img.shape[0] or row < 0 or col >= img.shape[1] or col < 0:
		return 0

	return img[row][col]

def bilinear(img, row, col):
	row_floor = floor(row)
	row_ceil = ceil(row)
	col_floor = floor(col)
	col_ceil = ceil(col)

	p1 = boundary(img, row_floor, col_floor)
	p2 = boundary(img, row_floor, col_ceil)
	p3 = boundary(img, row_ceil, col_floor)
	p4 = boundary(img, row_ceil, col_ceil)

	dx = abs(row - row_floor)
	dy = abs(col - col_floor)

	return (1-dx)*(1-dy)*p1 + (dx)*(1-dy)*p2 + (1-dx)*(dy)*p3 + (dx)*(dy)*p4
