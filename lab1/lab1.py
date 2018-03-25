import sys
import numpy as np
from skimage import io, color, measure, exposure
import matplotlib.pyplot as plt

file_name = sys.argv[1]

img_colored = io.imread(file_name)

img_gray = color.rgb2gray(img_colored)
img_gray = exposure.rescale_intensity(img_gray, out_range=(0.0, 255.0))
img_gray[img_gray < 255.0] = 0.0
#plt.imshow(img_gray)
#plt.imshow(img_gray, cmap="gray")
#plt.show()

contours = measure.find_contours(img_gray, 0.8)
fig, ax = plt.subplots()
ax.imshow(img_gray, interpolation="nearest", cmap=plt.cm.gray)
for n, contour in enumerate(contours):
	ax.plot(contour[:, 1], contour[:, 0], linewidth=1.3)
plt.show()

small_regions = []
medium_regions = []
large_regions = []
areas = []

label_img = measure.label(img_gray, neighbors=4, background=255)
regions = measure.regionprops(label_img)
print("Number of regions: %d" % (len(regions)))
for properties in regions:
	print("Region %d: Perimeter: %.1f Area: %d" % (properties.label, properties.perimeter, properties.area))

	areas.append(properties.area)

	if properties.area < 1500:
		small_regions.append(properties.label)
	elif properties.area < 3000:
		medium_regions.append(properties.label)
	else:
		large_regions.append(properties.label)

print("Small regions: %d" % (len(small_regions)))
print(small_regions)
print("Medium regions: %d" % (len(medium_regions)))
print(medium_regions)
print("Large regions: %d" % (len(large_regions)))
print(large_regions)

plt.hist(areas, bins="auto")
plt.title("Histogram of areas in %s" % (file_name))
plt.xlabel("Area")
plt.ylabel("Number os regions")
plt.savefig("histogram_" + file_name)
