import matplotlib.pyplot as plt
import numpy as np

def grafique(dictionaire):
    plt.figure()
    number = len(dictionaire.keys())
    #print(number)
    for i,key in zip(range(1,number+1),dictionaire.keys()):
        plt.subplot(number,1,i)
        plt.plot(dictionaire[key])

    plt.show()

dict1 = {f"experience {i}":np.random.randn(100,2) for i in range(4)}
grafique(dict1)
#print(dict1)