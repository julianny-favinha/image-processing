import numpy as np
from skimage import io
from boundary import boundary

def neighbor(img, row, col):
	return boundary(img, int(round(row)), int(round(col)))
