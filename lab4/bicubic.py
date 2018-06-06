import numpy as np
from math import floor
from skimage import io
from utilities import boundary, distances

def R(s):
	return (1/6)*(pow(P(s+2), 3) - 4*pow(P(s+1), 3) + 6*pow(P(s), 3) - 4*pow(P(s-1), 3))

def P(s):
	return s if s > 0 else 0

def bicubic(img, row, col):
	dx, dy = distances(row, col)

	value = 0.0
	for m in range(-1, 3):
		for n in range(-1, 3):
			p = boundary(img, int(floor(row) + m), int(floor(col) + n))
			
			value += p * R(m-dx) * R(dy-n)
		
	return int(round(value))
