import matplotlib.pyplot as plt
import numpy as np

def grafique(dictionaire):
    plt.figure()
    plt.subplot(4,1,1)
    plt.plot(dictionaire["experience 0"])

    # plt.subplot(4,1,2)
    # plt.plot(np.linspace(1,100,100),dictionaire["experience 1"])

    # plt.subplot(4,1,3)
    # plt.plot(np.linspace(1,100,100),dictionaire["experience 2"])

    # plt.subplot(4,1,4)
    # plt.plot(np.linspace(1,100,100),dictionaire["experience 3"])

    plt.show()

dict1 = {f"experience {i}":np.random.randn(100) for i in range(4)}
grafique(dict1)
print(dict1)