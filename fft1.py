from scipy import fftpack
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,30,1000)
y = 3*np.sin(x) + 2*np.sin(5*x)+ np.sin(10*x) + np.random.random(x.shape[0])*10

fourier = fftpack.fft(y)
power =np.abs(fourier)
freq = np.abs(fftpack.fftfreq(y.size))

#filtrage de spectre :
fourier[np.abs(fourier)< 400] = 0
filtred_signal = fftpack.ifft(fourier)

plt.figure(figsize=(12,8))

plt.plot(x,y)
plt.plot(x, filtred_signal,c='r')

plt.figure()
plt.plot(freq,power)

plt.show()
