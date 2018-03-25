import sys
import numpy as np
from skimage import io, color, measure, exposure
import matplotlib.pyplot as plt

file_name = sys.argv[1]

img_colored = io.imread(file_name)

img_gray = color.rgb2gray(img_colored)
#plt.imshow(img_gray, cmap="gray")
#plt.show()
img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))

contours = measure.find_contours(img_gray, 0.8)
#fig, ax = plt.subplots()
#ax.imshow(img_gray, interpolation="nearest", cmap=plt.cm.gray)
#for n, contour in enumerate(contours):
#	ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5)
#plt.show()

small_regions = []
medium_regions = []
large_regions = []
areas = []

label_img = measure.label(img_gray, neighbors=4)
regions = measure.regionprops(label_img)
print("Number of regions: %d" % (len(regions)-1))
for properties in regions[1:]:
	print("Region %d: Perimeter: %.1f Area: %d" % (properties.label - 2, properties.perimeter, properties.area))

	areas.append(properties.area)

	if properties.area < 1500:
		small_regions.append(properties.label - 2)
	elif properties.area < 3000:
		medium_regions.append(properties.label - 2)
	else:
		large_regions.append(properties.label - 2)

print("Small regions: %d" % (len(small_regions)))
print(small_regions)
print("Medium regions: %d" % (len(medium_regions)))
print(medium_regions)
print("Large regions: %d" % (len(large_regions)))
print(large_regions)

plt.hist(areas[1:], bins="auto")
plt.title("Histogram of areas in %s" % (file_name))
plt.xlabel("Areas")
plt.ylabel("Number os regions")
plt.savefig('histogram_' + file_name)
