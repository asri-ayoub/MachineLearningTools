import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_excel("titanic3.xls")
data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'], axis=1, inplace=True)
#print(data.head())
print(data['age'].mean())
data[data['age'] <= 20] = 0
data[data['age'] > 40] = 3
data[data['age'] > 30] = 2
data[data['age'] > 20] = 1

print(data['age'].value_counts())
