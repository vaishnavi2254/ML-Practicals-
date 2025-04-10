import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.datasets import load iris

iris load iris()

Xiris.data Features

yiris.target

df= pd.Dataframe (X, columns=iris.feature_names)

df[species] = y

print(df.head())

SX_train, X_test, y train, y_test = train_test split(X, y, test_size=0.2, random_state=47)

scaler = StandardScaler()

X_train scaler.fit_transform(X_train)

X test scaler.transform(X_test)

k=5

knn KNeighborsClassifier(n_neighbors=k)

knn.fit(X train, y train)

KNeighborsClassifier

KNeighborsClassifier()

y pred knn.predict(X_test)

accuracy accuracy_score(y_test, y_pred) print(f"Accuracy: accuracy 100:.24 %")

Accuracy: 100.00%

print("\nClassification Report:")

print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")

print(confusion_matrix(y_test, y_pred))

print("\nCorrect and Incorrect Predictions:")

for i in range(len(y_test)):

correct y_test[i] == y pred[i]

print(f"Actual: (iris.target_names[y_test[i]]), Predicted: (iris.target_names[y_pred[1]]]

['Correct' if correct else "wrong")")