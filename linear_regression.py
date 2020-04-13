import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

np.random.seed(0)
m = 100
x = np.linspace(0,10,m).reshape(m,1)
y = x**2 + np.random.randn(m,1)

object = SVR(C=100)
object.fit(x,y)
print(object.score(x,y))
y_p = object.predict(x)

plt.figure()

plt.scatter(x,y)
plt.plot(x, y_p, c ='r',lw = 2)

plt.show()