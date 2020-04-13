import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split, GridSearchCV, learning_curve#validation_curve (optional)
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

# créer un train set puis un test set, entrainez puis évaluez
# Avec gridsearch, trouvez les meilleurs hyper paramètres; n_nighbr.. , metrics et weight
# est ce que collecter plus de données serait utile ?