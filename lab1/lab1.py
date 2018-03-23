import sys
import numpy as np
from skimage import io, color, measure
import matplotlib.pyplot as plt

#file_name = sys.argv[1]
file_name = "objetos1.png"

# open image
img_colored = io.imread(file_name)
#plt.show()

# The resulting image is a grayscale image. imshow is using, by default, a kind of heatmap (called vidris) to display the image intensities if we don't use cmap="gray".
img_gray = color.rgb2gray(img_colored)
#plt.imshow(img_gray)
#plt.show()
#plt.imshow(img_gray, cmap="gray")
#plt.show()

# find and plot all the contours of the objects inside the image
contours = measure.find_contours(img_gray, 0.8)

fig, ax = plt.subplots()
ax.imshow(img_gray, interpolation='nearest', cmap=plt.cm.gray)
# n é o numero de contornos obtidos
for n, contour in enumerate(contours):
	print(n)
	#print("perimetro[%d] = %f" % (n, measure.perimeter(contour, neighbourhood=4)))
	ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5)
#plt.show()
