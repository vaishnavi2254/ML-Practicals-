impart numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing

from sklearn.preprocessing import Polynomial Features

from sklearn.linear model import Linear Regression

from sklearn.metrics import mean_squared_error

from sklearn.model selection import train test split

california fetch california housing()

data pd.DataFrame(california.data, columns=california.feature_names)

data "MEDV california.target"

X data "MedInc.values"

y data "MEDV values"

X train, X_test, y train, y_test train_test_split(X, y, test size=0.2, random_state=42)

degree=3
# Change degree as needed

poly Polynomial Features (degree=degree)

X_train polypoly.fit transform(X_train)

X_test poly poly.transform(X_test)

model LinearRegression()

model.fit(X_train poly, y_train)

y pred model.predict(X_test poly)

mse mean_squared_error(y_test, y_pred)

print('Mean Squared Error: (mse)')

Mean Squared Error: 0.6982964744960335

plt.scatter(X, y, colors'blue', label Original Data')

sorted indices np.argsort(X_train.flatten())

plt.plot(X_train, flatten() sorted_indices), model.predict(X_train_poly) sorted_indices, color='red', label='Regression Curve')

plt.xlabel('Median Income (MedInc)')

plt.ylabel('Median House Value (MFDV)')

plt.title('Non-Linear Regression on California Housing Dataset')

plt.legend()

pit.show()
