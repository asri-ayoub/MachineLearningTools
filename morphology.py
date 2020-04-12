from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np 

np.random.seed(0)
image = np.zeros((32,32))
image[10:-10,10:-10] = 1
image[np.random.randint(0,32,30),np.random.randint(0,32,30)] = 1
image_bo = ndimage.binary_opening(image)

plt.figure(); plt.imshow(image)

plt.figure(); plt.imshow(image_bo)

plt.show()