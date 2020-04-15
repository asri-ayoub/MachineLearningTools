import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve, cross_val_score, validation_curve#validation_curve (optional)
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 

# créer un train set puis un test set, entrainez puis évaluez
# Avec gridsearch, trouvez les meilleurs hyper paramètres; n_nighbr.. , metrics et weight
# est ce que collecter plus de données serait utile ?
data = pd.read_excel("titanic3.xls")
data = data[["pclass","survived","sex","age"]]
data.dropna(axis=0, inplace=True)
target = data["survived"]
data.drop("survived", axis=1, inplace = True)
data["sex"].replace(["male","female"],[0,1], inplace = True)

X_train, X_test, y_train, y_test = train_test_split(data,target)

object = GridSearchCV(KNeighborsClassifier(),{"n_neighbors":range(1, 20)}, cv = 5)
object.fit(X_train, y_train)

print(object.best_estimator_)
print(object.best_score_)
print(object.best_params_["n_neighbors"])
print(object.best_index_)