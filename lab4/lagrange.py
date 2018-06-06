import numpy as np
from math import floor
from skimage import io
from utilities import boundary, distances

def L(img, n, dx, row, col):
	p1 = (-dx*(dx-1)*(dx-2)*boundary(img, row-1, col+n-2))/6
	p2 = ((dx+1)*(dx-1)*(dx-2)*boundary(img, row, col+n-2))/2
	p3 = (-dx*(dx+1)*(dx-2)*boundary(img, row+1, col+n-2))/2
	p4 = (dx*(dx+1)*(dx-1)*boundary(img, row+2, col+n-2))/6

	return p1 + p2 + p3 + p4

def new_intensity(img, dx, dy, row, col):
	l1 = L(img, 1, dx, row, col)
	l2 = L(img, 2, dx, row, col)
	l3 = L(img, 3, dx, row, col)
	l4 = L(img, 4, dx, row, col)

	f1 = (-dy*(dy-1)*(dy-2)*l1)/6
	f2 = ((dy+1)*(dy-1)*(dy-2)*l2)/2
	f3 = (-dy*(dy+1)*(dy-2)*l3)/2
	f4 = (dy*(dy+1)*(dy-1)*l4)/6

	return f1 + f2 + f3 + f4

def lagrange(img, row, col):
	dx, dy = distances(row, col)

	return new_intensity(img, dx, dy, floor(row), floor(col))
