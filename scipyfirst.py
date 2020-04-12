from scipy import misc
import matplotlib.pyplot as plt 

face = misc.face(gray=True)
print(face.shape)
# plt.imshow(face,cmap=plt.cm.gray)
# plt.show()

raw,col = face.shape
face2 = face[raw//3:-raw//3, col//3:-col//3]

face3 = face2[face2>250]
face3 = face2
face3[face3>150] = 255
plt.imshow(face2,cmap=plt.cm.gray)

plt.figure()
plt.hist(face3)
plt.show()