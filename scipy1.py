from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,10,10)
y = x**2

f = interp1d(x,y,kind='linear')#kind: type d'interpolation (ex: cubic)

x_i = np.linspace(1,10,30)
y_i = f(x_i)

plt.figure()
plt.scatter(x,y)
plt.title("origin data")

plt.figure()
plt.scatter(x_i,y_i)
plt.title("interpolated data")

plt.show()