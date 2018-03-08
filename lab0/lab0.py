import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# img file
img_file = sys.argv[1]

# open image file and stores it in a numpy array
img = misc.imread(img_file)

# compute histogram of img
bins = np.arange(0, 255, 1)
frq, edges = np.histogram(img.flatten(), bins)

# plot and save histogram
ax = plt.subplot()
ax.bar(edges[:-1], frq, width=np.diff(edges))
plt.xlabel("Grayscale")
plt.ylabel("Frequency")
plt.savefig(img_file.replace('.png', '') + '_histogram.png')

# show image statistics
print("(Width, Height): ", img.shape)
print("Minimum intensity: ", img.min())
print("Maximum intensity: ", img.max())
print("Medium intensity: ", img.mean())

# negative image
img_negative = 255 - img
misc.imsave(img_file.replace('.png', '') + '_negative.png', img_negative)

# new intensity interval image
img_new_intensity = (60/255)*img + 120
misc.imsave(img_file.replace('.png', '') + '_new_intensity.png', img_new_intensity)
