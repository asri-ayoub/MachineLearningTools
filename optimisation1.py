from scipy.optimize import curve_fit,minimize
import numpy as np
import matplotlib.pyplot as plt

def f_model(x,a,b,c,d):
    return a*x**3 +b*x**2 + c*x + d

x = np.linspace(0,2,100)
y = 1/3*x**3 - 3/5*x**2 + 2 + np.random.randn(x.shape[0])/20
arg, cov = curve_fit(f_model,x,y)

plt.figure()

plt.scatter(x,y)
plt.plot(x,f_model(x,arg[0],arg[1],arg[2],arg[3]),c='r')

############ Minimization #########""

def f(x):
    return x**2 + 15* np.sin(x)

def f1(x):
    return np.sin(x[0]) + np.cos(x[0]+x[1])*np.cos(x[0])

xf1 = np.linspace(-3,3,100)
yf1 = np.linspace(-3,3,100)

xx,yy = np.meshgrid(xf1, yf1)
x0f1 = np.zeros((2,1))
resultf1 = minimize(f1,x0f1).x

x1 = np.linspace(-10,10,100)
x0 = -4
result = minimize(f,x0=x0).x

plt.figure()
plt.plot(x1,f(x1))
plt.scatter(result,f(result),s=100,c='r', zorder=1)
plt.scatter(x0,f(x0),marker='+',c='g',s=200, zorder=1)

plt.figure()
plt.contour(xx,yy,f1(np.array([xx,yy])),20)
plt.scatter(x0f1[0],x0f1[1],marker='+',c='g',s=200, zorder=1)
plt.scatter(resultf1[0],resultf1[1],s=100,c='r', zorder=1)
plt.show()
