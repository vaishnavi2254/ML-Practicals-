import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier, export text

from sklearn import tree

import matplotlib.pyplot as pit

data = pd.DataFrame([
["Sunny", "Hot", "High', 'Weak', 'No'),]

['Sunny', 'hot', "High", "Strong", "No"],
["Overcast", "Hot", 'High', 'Meak', 'Yes'],
['Rain', "Mild", "High", "Weak', 'Yes'],
["Rain", "Cool", "Normal', 'Weak", "Yes"],
["Rain", "Cool", "Normal', 'Strong', 'No],
["Overcast", "Cool", 'Normal', 'Strong', 'Yes'],
[ "Sunny", "Mild", "High", "Weak', 'No'],
["Sunny", "Cool", "Normal", "Weak', 'Yes'],
["Rain", "Mild', 'Normal', 'Wook", "Yes"],
["Sunny", "Mild", "Normal", "Strong", "Yes"],
["Overcast", "Mild", "High", "Strong', 'Yes'],
["Overcast', 'Hot', "Normal", "Weak", "Yes"],
["Rain", "Mild', 'High', 'Strong', 'No"] ,
], columns = [Outlook", "Temperature', 'Humidity', 'Wind', 'PlayTennis"])

le = LabelEncoder()

for column in data.columns:

data [column]= le.fit transform(data[column))

x = data.drop("PlayTennis', axis=1)

y = data ['PlayTennis']

model= DecisionTreeClassifier(criterions = 'gini', max_depths))

model= DecisionTreeClassifier(criterion='gini', max_depth=3)
model.fit(X, y)

Decision Treeclassifier

DecisionTreeClassifier(max_depth=3)

pls.figure(figsize=(12,8))
tree plot tree(model, feature_names=X.columns, class_names=['No', 'Yes'), filled=True)
plt.title("CART Decision Tree (Gini Index)")
plt.show()