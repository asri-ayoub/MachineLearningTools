import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as dataset
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = dataset.load_iris()

data = iris.data
target = iris.target
x_train, x_test, y_train, y_test = train_test_split(data,target, test_size=0.2, random_state=5)
print(x_train.shape, x_test.shape)
model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)
print(model.score(x_train,y_train))
print(model.score(x_test,y_test))


plt.figure()
plt.subplot(2,1,1)
plt.scatter(x_train[:,0], x_train[:,1], c=y_train)

plt.subplot(2,1,2)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test)

plt.show()

print(data.shape)

