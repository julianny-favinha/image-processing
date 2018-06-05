import sys, getopt



def read_parameters(argv):
	# -a
	angle = 0.0

	# -e
	scale = 0.0

	# -d
	width, height = (0, 0)

	# -m
	mode = ""

	# -i
	img_input_name = ""

	# -o
	img_output_name = ""
   
	opts, args = getopt.getopt(argv, "a:e:d:m:i:o")

	for opt, arg in opts:
		if opt == "-a":
			angle = arg
		if opt == "-e":
			scale = arg
		# TODO parse errado
		if opt == "-d":
			width, length = arg
		if opt == "-m":
			mode = arg
		if opt == "-i":
			img_input_name = arg
		if opt == "-o":
			img_output_name = arg

if __name__ == "__main__":
	read_parameters(sys.argv[1:])
