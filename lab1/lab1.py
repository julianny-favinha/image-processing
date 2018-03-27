import sys
import numpy as np
from skimage import io, color, measure, exposure
import matplotlib.pyplot as plt

# reads file image
file_name = sys.argv[1]
img_colored = io.imread(file_name)

# transform rgb image to grayscale
img_gray = color.rgb2gray(img_colored)
img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

# transform grayscale image to black (0) and white (255) image. every pixel < 255 is an object (in this case)
img_gray[img_gray < 255] = 0

# save black and white image
fig = plt.imshow(img_gray, cmap="gray")
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig(file_name.replace(".png", "") + "_blackandwhite.png", bbox_inches="tight")

# find contours of each object
contours = measure.find_contours(img_gray, level=0.5)
fig, ax = plt.subplots()
plt.imshow(img_gray, interpolation="nearest", cmap=plt.cm.gray)
for n, contour in enumerate(contours):
	ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.savefig(file_name.replace(".png", "") + "_contours.png", bbox_inches="tight")

small_regions = []
medium_regions = []
large_regions = []
areas = []

# find properties for each object
labels = measure.label(img_gray, neighbors=4, background=255)
regions = measure.regionprops(labels)

# plot image with grayscale changed to put labels in the objects
plt.clf()
fig = plt.imshow(exposure.rescale_intensity(img_colored, out_range=(200, 255)))

print("Number of regions: %d" % (len(regions)))

for properties in regions:
	# print properties
	print("Region %d: Perimeter: %.1f Area: %d" % (properties.label, properties.perimeter, properties.area))

	# sort objects by area
	if properties.area < 1500:
		small_regions.append(properties.label)
	elif properties.area < 3000:
		medium_regions.append(properties.label)
	else:
		large_regions.append(properties.label)

	# add objects area to array to plot histogram later 
	areas.append(properties.area)

	# plot label of object inside the object using the centroid
	plt.text(properties.centroid[1]-8, properties.centroid[0]+2, str(properties.label), fontsize=8)
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig(file_name.replace(".png", "") + "_labelled.png", bbox_inches="tight")

# print labels of small, medium and large regions
print("Small regions: %d" % (len(small_regions)))
print(small_regions)
print("Medium regions: %d" % (len(medium_regions)))
print(medium_regions)
print("Large regions: %d" % (len(large_regions)))
print(large_regions)

# save histogram of areas
plt.clf()
plt.hist(areas, bins=[0, 1500, 3000, 4500])
plt.title("Histogram of areas in %s" % (file_name))
plt.xlabel("Area")
plt.ylabel("Number os regions")
plt.savefig(file_name.replace(".png", "") + "_histogram.png")
