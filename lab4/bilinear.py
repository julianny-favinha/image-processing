import numpy as np
from math import ceil, floor
from skimage import io
from utilities import boundary, distances

def bilinear(img, row, col):
	p1 = boundary(img, floor(row), floor(col))
	p2 = boundary(img, floor(row), ceil(col))
	p3 = boundary(img, ceil(row), floor(col))
	p4 = boundary(img, ceil(row), ceil(col))

	dx, dy = distances(row, col)

	return (1-dx)*(1-dy)*p1 + (dx)*(1-dy)*p2 + (1-dx)*(dy)*p3 + (dx)*(dy)*p4
