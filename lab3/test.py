from skimage import io, filters, color, exposure
import numpy as np
import matplotlib.pyplot as plt
import sys

# parametros de entrada
img_input_name = sys.argv[1]

# le a imagem de entrada
img = io.imread(img_input_name)


print (img[:,:,3])
img[:,:,3] = 0


io.imsave("withoutalpha.png", img)




#imgwithoutalpha = img[:,:,:3]

#imgfiltered = filters.gaussian(img, sigma=1, multichannel=True)
#imgwithoutalphafiltered = filters.gaussian(imgwithoutalpha, sigma=1, multichannel=True)
#io.imsave("imgfiltered.png", imgfiltered)
#io.imsave("imgwithoutalphafiltered.png", imgwithoutalphafiltered)

#imgfiltered[imgfiltered < 255] = 0
#imgwithoutalphafiltered[imgwithoutalphafiltered < 255] = 0


#io.imsave("imgfilteredbinarized.png", imgfiltered)
#io.imsave("imgwithoutalphafilteredbinarized.png", imgwithoutalphafiltered)


img_gray = color.rgb2gray(img)
#io.imsave("gray.png", img_gray)

"""img_gray = exposure.rescale_intensity(img_gray, out_range=(0, 255))
print(img_gray)
bins = np.arange(0, 255, 1)
frq, edges = np.histogram(img.flatten(), bins)
ax = plt.subplot()
ax.bar(edges[:-1], frq, width=np.diff(edges))
plt.xlabel("Grayscale")
plt.ylabel("Frequency")
plt.savefig('histogram.png')"""

"""print("-------------------------")
val = img_gray[20][20]

rows = img.shape[0]	
cols = img.shape[1]

for row in range(0, 2):
	for col in range(0, 2):
		pixel = img_gray[row][col] 
		print(pixel < 10)

io.imsave("test.png", img_gray)"""

dic = {}
values = [1,2,3,4,5,5,5,5,3,2]

for val in values:
	if val not in dic:
		dic[val] = 1 
	else:
		dic[val] += 1

print(dic)

print(max(dic, key=dic.get))
