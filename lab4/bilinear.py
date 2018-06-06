import numpy as np
from math import ceil, floor
from skimage import io

def bilinear(img, row, col):
	row_floor = floor(row)
	row_ceil = ceil(row) if ceil(row) < img.shape[0] else img.shape[0]-1
	col_floor = floor(col)
	col_ceil = ceil(col) if ceil(col) < img.shape[1] else img.shape[1]-1

	p1 = img[row_floor][col_floor]
	p2 = img[row_floor][col_ceil]
	p3 = img[row_ceil][col_floor]
	p4 = img[row_ceil][col_ceil]

	dx = abs(row - row_floor)
	dy = abs(col - col_floor)

	return (1-dx)*(1-dy)*p1 + (dx)*(1-dy)*p2 + (1-dx)*(dy)*p3 + (dx)*(dy)*p4
