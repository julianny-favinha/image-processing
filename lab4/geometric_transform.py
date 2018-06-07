import argparse
import numpy as np
from skimage import io

from neighbor import neighbor
from bilinear import bilinear
from bicubic import bicubic
from lagrange import lagrange

def read_parameters():
	parser = argparse.ArgumentParser()

	parser.add_argument("-a", "--angle", type=float, help="angle in degrees to rotate image")
	parser.add_argument("-e", "--scale", type=float, help="scale to shrink or extend image")
	parser.add_argument("-d", "--dimensions", nargs=2, type=int, help="width and height of new image")
	parser.add_argument("-m", "--mode", type=str, help="Interpolation {neighbor, bilinear, bicubic, lagrange}")
	parser.add_argument("-i", "--inputname", type=str, help="Image input name")
	parser.add_argument("-o", "--outputname", type=str, help="Image output name")

	args = parser.parse_args()
	return args

if __name__ == "__main__":
	# parse dos parametros
	args = read_parameters()

	angle = args.angle
	scale = args.scale
	dimensions = args.dimensions
	mode = args.mode
	inputname = args.inputname
	outputname = args.outputname

	# le a imagem de entrada
	img = io.imread(inputname)
	if dimensions is None:
		dimensions = (img.shape[0], img.shape[1])

	# calcula as dimensoes da nova imagem
	if scale is not None:
		dimensions = (int(img.shape[0]*scale), int(img.shape[1]*scale))

	if angle is not None:
		matrix = np.array([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))], [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]])
	else:
		matrix = np.array([[dimensions[1] / img.shape[1], 0.0], [0.0, dimensions[0] / img.shape[0]]])

	inverse = np.linalg.inv(matrix)

	# nova imagem
	new_img = np.zeros(shape=(dimensions[1], dimensions[0]), dtype=np.uint8)
 
	for row in range(0, new_img.shape[0]):
		for col in range(0, new_img.shape[1]):
			coord = np.array([[row], [col]])
			new_coord = inverse @ coord

			if mode == "neighbor":
				new_img[row][col] = neighbor(img, new_coord.ravel()[0], new_coord.ravel()[1])
			elif mode == "bilinear":
				new_img[row][col] = bilinear(img, new_coord.ravel()[0], new_coord.ravel()[1])
			elif mode == "bicubic":
				new_img[row][col] = bicubic(img, new_coord.ravel()[0], new_coord.ravel()[1])
			else:
				new_img[row][col] = lagrange(img, new_coord.ravel()[0], new_coord.ravel()[1])

	io.imsave(outputname, new_img)
