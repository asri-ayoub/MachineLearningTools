from scipy import signal
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,20,100)
y = x + 4 * np.sin(x) + np.random.randn(x.shape[0])
y_no_trend = signal.detrend(y)

plt.figure()

plt.plot(x,y)
plt.plot(x,y_no_trend,c='r')

plt.show()