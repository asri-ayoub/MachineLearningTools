import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

image = ndimage.imread("bacteria.jpg")
#RGB to gray
image = image[:,:,0] 

### hist
image_copy = np.copy(image)


print(image.shape)

plt.figure()
plt.imshow(image)

plt.figure()
plt.hist(image_copy.ravel(),bins=255)

# extract only bacteries
image = image < 150

# delete artifacts
image = ndimage.binary_opening(image)

plt.figure()
plt.imshow(image)

# extract labels
image_labeled,label_number = ndimage.label(image)

plt.figure()
plt.imshow(image_labeled)

#sum labels (to evaluate the size of each bateria)
sizes = ndimage.sum(image,image_labeled,range(label_number))
plt.figure()
plt.scatter(range(label_number), sizes)

plt.show()