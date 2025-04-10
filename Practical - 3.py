import pandas as pd

file_path "TY/Salary_dataset.csv"

df pd.read_csv("Salary_dataset.csv")

print(df.head())

print(df.info())

print(df.describe())

import numpy as np

from sklearn.model selection import train_test_split

from sklearn.linear_model import LinearRegression

model-LinearRegression()

y_pred=model.predict(x_test)

comparison=pd.DataFrame('Actual': y_test, 'Predicted: y_pred))

print(comparison.head())

from sklearn.metrics import mean squared error

mse mean squared_error(y_test, y_pred)

print("Mean Squared Error: (mse")


