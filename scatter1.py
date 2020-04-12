import matplotlib.pyplot as plt 
import numpy as np
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
from scipy import misc

iris = load_iris()
x = iris.data # col0: longueur, col1: largeur, col2: taille pétale
y = iris.target
names = iris.target_names

#print(x)
#print(names[0])

# plt.figure()
# plt.scatter(x[:,0],x[:,1],c=y,alpha = 0.5, s = x[:,2]*100)# alpha est la transparence des points # s est la taille des point
# plt.xlabel("longeur sépal")
# plt.ylabel("largeur sépal")

# plt.show()

####################
print("########### 3D ###########")

#plt.figure()
# ax = plt.axes(projection = '3d')
# ax.scatter(x[:,0],x[:,1],x[:,2], c=y)
#plt.show()

##### plot_surface #########
# f = lambda x,y:np.sin(x) + np.cos(x+y)
# plt.figure()
# X = np.linspace(1,5,100)
# Y = np.linspace(1,5,100)
# XX,YY = np.meshgrid(X,Y)
# Z = f(XX,YY)
# ax = plt.axes(projection='3d')
# ax.plot_surface(XX,YY,Z,cmap='plasma')

# plt.show()

########### Histogram ######
plt.figure()
plt.hist(x[:,0],bins=30)
plt.hist(x[:,1],bins=30)
#2D hist
plt.figure()
plt.hist2d(x[:,0],x[:,1],cmap = 'Blues')
plt.colorbar()

plt.figure()
image = misc.face(gray=True)
plt.hist(image.ravel(), bins=255)


######## contour ########


######## Imshow #########

plt.figure()
plt.imshow(np.corrcoef(x.T),cmap='Blues')
plt.colorbar()
plt.show()