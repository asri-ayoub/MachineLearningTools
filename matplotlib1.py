import matplotlib.pyplot as plt
import numpy as np 


x = np.linspace(0,2,10)
y = x**2

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.plot(x,y,c='red',lw=3,ls='--',label='quadratique') #lw: lane width #ls: lane style ('--',)
plt.plot(x,x**3,c='blue',label='cubique')
plt.title("notre super graphe")
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.subplot(2,1,2)
plt.plot(x,np.cos(x))
plt.plot(x,np.sin(x))
plt.title("notre 2ème super graphe")
#plt.scatter(x,y)
plt.show()
#plt.savefig("fig_enregistre")