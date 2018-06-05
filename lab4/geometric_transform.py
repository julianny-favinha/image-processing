import argparse

from neighbor import neighbor
from bilinear import bilinear
from bicubic import bicubic
from lagrange import lagrange

def create_dict(angle, scale, dimensions, mode, inputname, outputname):
	dic = {}

	dic["angle"] = angle
	dic["scale"] = scale
	dic["dimensions"] = dimensions
	dic["mode"] = mode
	dic["inputname"] = inputname
	dic["outputname"] = outputname

	return dic

def read_parameters():
	parser = argparse.ArgumentParser()

	parser.add_argument("-a", "--angle", type=float, help="angle in degrees to rotate image")
	parser.add_argument("-e", "--scale", type=float, help="scale to shrink or extend image")
	parser.add_argument("-d", "--dimensions", nargs=2, type=int, help="width and height of new image")
	parser.add_argument("-m", "--mode", type=str, help="Interpolation {neighbor, bilinear, bicubic, lagrange}")
	parser.add_argument("-i", "--inputname", type=str, help="Image input name")
	parser.add_argument("-o", "--outputname", type=str, help="Image output name")

	args = parser.parse_args()

	return create_dict(args.angle, args.scale, args.dimensions, args.mode, args.inputname, args.outputname)

if __name__ == "__main__":
	# parse dos parametros
	dic = read_parameters()

	if dic["mode"] == "neighbor":
		neighbor(dic)
	elif dic["mode"] == "bilinear":
		bilinear(dic)
	elif dic["mode"] == "bicubic":
		bicubic(dic)
	else:
		lagrange(dic)
