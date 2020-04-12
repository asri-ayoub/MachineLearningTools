import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

image = ndimage.imread("bacteria.jpg")

### hist
image_copy = np.copy(image)


print(image.shape)

plt.figure()
plt.imshow(image)

plt.figure()
plt.hist(image_copy.ravel(),bins=255)

plt.show()