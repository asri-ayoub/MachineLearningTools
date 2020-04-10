import numpy as np 
def matrix(row, colomn):
    result = np.random.randn(row,colomn)
    return np.concatenate((result,np.ones((row,1))), axis=1)

vect = np.array([1,2,3,4,5,6])
print(vect.shape); print(vect.reshape(6,1).shape); print(vect.squeeze().shape)

vect2d = np.zeros((5,2))
print(vect2d)
vectrand = np.random.randn(4,4)
print(vectrand)
print(vect2d.size)
print( np.linspace(1,10))
print(np.arange(1,10,2))
print("squeeze : ",vect2d.ravel())
print("########exercice#####")
print(matrix(3,3))

