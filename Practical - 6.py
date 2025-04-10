import pandas as pd

from sklearn.model_selection import train test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.naive bayes import GaussianNB

from sklearn.metrics import accuracy score, confusion matrix, classification report

from sklearn import datasets

iris datasets.lood iris()

data pd.DataFrame(iris.data, columns=iris.feature_names)

data['label'] = iris.target

X data.iloc[:, :-1].values

y= data. iloc:, -1).values

X_train, X_test, y train, y_test = train test split(X, y, test_size=8.2, random_state=42)

model GaussianNB()

model.fit(X_train, y_train)

GaussianNB

GaussianNB()

y_pred model.predict(X-test)

accuracy accuracy_score(y_test, y_pred)

print("Accuracy of Naive Bayes classifier:", accuracy)

accuracy accuracy score(y_test, y pred)

print("Accuracy of Naive Bayes classifier:", accuracy)


rix(y_test, y_pred)) print("Confusion Matrix:\n", confusion matrix(y_test,

print("Classification Report:\n", classification report(y_test, y_pred, target_names=iris.target_names))

print("Confusion Matrix:\n", confusion matrix(y_test,

print("Classification Report:\n", classification report(y_test, y_pred, target_names=iris.target_names))