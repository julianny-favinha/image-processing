import numpy as np
from math import floor
from skimage import io

def R(s):
	return (1/6)*(pow(P(s+2), 3) - 4*pow(P(s+1), 3) + 6*pow(P(s), 3) - 4*pow(P(s-1), 3))

def P(s):
	return s if s > 0 else 0

def boundary(img, row, col):
	if row >= img.shape[0] or row < 0 or col >= img.shape[1] or col < 0:
		return 0

	return img[row][col]

def bicubic(img, row, col):
	dx = abs(row - floor(row))
	dy = abs(col - floor(col))

	value = 0.0
	for m in range(-1, 3):
		for n in range(-1, 3):
			p = boundary(img, int(floor(row) + m), int(floor(col) + n))
			
			value += p * R(m-dx) * R(dy-n)
		
	return int(round(value))
