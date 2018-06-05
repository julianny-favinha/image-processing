import argparse

def read_parameters():
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--angle", type=float, help="angle in degrees to rotate image")
	parser.add_argument("-e", "--scale", type=float, help="scale to shrink or extend image")
	parser.add_argument("-d", "--dimensions", nargs="+", type=int, help="width and height of new image")
	parser.add_argument("-m", "--mode", type=str, help="{neighbor, bilinear, bicubic, lagrange}")
	parser.add_argument("-i", "--inputname", type=str, help="Image input name")
	parser.add_argument("-o", "--outputname", type=str, help="Image output name")
	args = parser.parse_args()
	print (args)

if __name__ == "__main__":
	read_parameters()
