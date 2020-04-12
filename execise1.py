import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

def grafique(dictionaire):
    plt.figure()
    number = len(dictionaire.keys())
    #print(number)
    for i,key in zip(range(1,number+1),dictionaire.keys()):
        plt.subplot(number,1,i)
        plt.plot(dictionaire[key])

    plt.show()

def grafiqueIris(dataset):
    data = dataset.data
    target = dataset.target
    n = data.shape[1]

    plt.figure(figsize=(12,8))
    
    for i in range(1,n+1):
        plt.subplot(n,1,i)
        plt.scatter(data[:,0],data[:,i-1],c=target)
        plt.xlabel('longeur sépal')
        plt.ylabel(i)
        plt.colorbar(ticks = list(np.unique(target)))

    plt.show()

dict1 = {f"experience {i}":np.random.randn(100,2) for i in range(4)}
#grafique(dict1)

data = load_iris()
grafiqueIris(data)