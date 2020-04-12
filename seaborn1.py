import seaborn as sns
import matplotlib.pylab as plt
import numpy as np 
import pandas as pd

data = pd.read_csv("IRIS.csv")
print(data.head())
sns.pairplot(data,hue='setosa')
plt.show()