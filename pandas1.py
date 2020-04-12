import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_excel("titanic3.xls")
print(data.shape)

data = data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'],axis=1)
print(data.head())
data = data.dropna(axis=0)
print(data.describe())
print(data['pclass'].value_counts())

data['pclass'].value_counts().plot.bar()

plt.figure()
data['age'].hist()
plt.show()

print(data.groupby(['sex','pclass']).mean())