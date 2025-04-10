import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear model import LogisticRegression

from sklearn.metrics import accuracy score, confusion_matrix, classification_report

from sklearn import datasets

[5]: iris datasets.load_iris()

Xiris.data

yiris.target

[6]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test size:0.2, random_state=42)

[7]:

scaler StandardScaler()

X train scaler.fit_transform(X_train)

X test scaler.transform(X_test)

[14]

model LogisticRegression(multi_class='ovr', solver='lbfgs', max_iter=200)

model.fit(X train, y_train)
LogisticRegression(max_iter=200, multi_class='ovr')
y_pred model.predict(X_test)

accuracy accuracy_score(y_test, y_pred)

print("Accuracy of the Logistic Regression model:", accuracy)
conf_matrix confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n", conf_matrix)
class_report = classification_report (y_test, y_pred)

print("Classification Report:\n", class_report)