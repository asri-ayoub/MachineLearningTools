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

print("######## PART2 #######")
A = np.random.randint(1,10,(10,10))
Abool = A<5
A[::2,0] = -1
print(A[A<5])

print("######## PART3 #######")

B = np.random.randint(0,10,(5,5))
print(B)
values, count = np.unique(B, return_counts = True)
for v,c in zip(values[np.argsort(count)], count[np.argsort(count)]):
    print(f"la valeur {v} apparait {c} fois")

print("######## Exercice 2 #######")
np.random.seed(0)
C = np.random.randint(0,100,[10,5])
print(C)
col = 0
stdc = np.zeros((1,5))
# while col < C.shape[1]:
#     stdc[col] = np.std(C[:,col])
#     col +=1

print(np.mean(C,axis=0))
print(np.std(C,axis=0))
print((C - np.mean(C,axis=0))/np.std(C,axis=0))