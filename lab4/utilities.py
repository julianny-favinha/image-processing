def distances(row, col):
	return row - floor(row), col - floor(col)

def boundary(img, row, col):
	if row >= img.shape[0] or row < 0 or col >= img.shape[1] or col < 0:
		return 255

	return img[row][col]