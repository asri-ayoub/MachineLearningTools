import numpy as np 
from sklearn.neighbors import  KNeighborsClassifier
import pandas as pd

def WouldVeSurvived(model, pclass = 3, sex=0, age=26):
    a = np.array([pclass, sex, age]).reshape(1,3)
    result = model.predict(a)
    print(model.predict_proba(a))

    if(result == 1):
        print("you would have survived in the titanic ! :)")
    else:
        print("you wouldn't have survived.. sorry :( ")

def paramSelection(features,label):
    results = {}
    for i in range(1,11):
        model = KNeighborsClassifier(i)
        model.fit(features, label)
        results[i]=model.score(features,label)
    print(results)


data = pd.read_excel("titanic3.xls")
data = data[["pclass","survived","sex","age"]]
data.dropna(axis=0, inplace = True)
data["sex"].replace(["male","female"],[0,1],inplace = True)

object = KNeighborsClassifier()
survived = data["survived"]
data.drop("survived",axis=1, inplace = True)
#print(data.head())

object.fit(data,survived)
print(object.score(data,survived))
WouldVeSurvived(object)
paramSelection(data, survived)