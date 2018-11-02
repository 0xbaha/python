# http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

balance_data = pd.read_csv(
'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
                           sep= ',', header= None)

print("Dataset Lenght:: ", len(balance_data))
print("Dataset Shape:: ", balance_data.shape)

print("Dataset:: ")
print(balance_data.head())
print()
X = balance_data.values[:, 1:5]
Y = balance_data.values[:,0]
print('X =\n',X)
print()
print('Y =\n',Y)
print()
# The parameter test_size is given value 0.3;
# it means test sets will be 30% of whole dataset  &
# training dataset’s size will be 70% of the entire dataset.
# random_state variable is a pseudo-random number generator state used
# for random sampling.
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
# Decision Tree Classifier with criterion gini index
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                                    max_depth=3, min_samples_leaf=5)
print('clf_gini.fit(X_train, y_train):\n',clf_gini.fit(X_train, y_train))
print()
# Decision Tree Classifier with criterion information gain
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
                                        max_depth=3, min_samples_leaf=5)
print('clf_entropy.fit(X_train, y_train):\n',clf_entropy.fit(X_train, y_train))
print()
# try to predict target variable for test set’s 1st record
print('clf_gini.predict([[4, 4, 3, 3]]):\n',clf_gini.predict([[4, 4, 3, 3]]))
print()
# Prediction for Decision Tree classifier with criterion as gini index
y_pred = clf_gini.predict(X_test)
print('y_pred\n',y_pred)
print()
# Prediction for Decision Tree classifier with criterion as information gain
y_pred_en = clf_entropy.predict(X_test)
print('y_pred_en\n',y_pred_en)
print()
# Accuracy for Decision Tree classifier with criterion as gini index
print("Accuracy is ", accuracy_score(y_test,y_pred)*100)
# Accuracy for Decision Tree classifier with criterion as information gain
print("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)
