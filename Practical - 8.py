import pandas as pd
Import numpy as np
from math import log2
import pprint

data = pd.DataFrame([
['Sunny', 'Hot', 'High', 'Strong', 'No']'
['Sunny', 'Hot', 'High', 'Strong', 'No'],
['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
['Rain', 'Mild', 'High", "Weak', 'Yes'],
['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
['Rain', 'Cool', 'Normal', 'Strong', 'No'],
["Overcast', 'Cool', 'Normal', 'Strong', 'Yes"],
['Sunny', 'Mild', 'High", "Weak", "No"],
['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
['Rain', 'Mild', "Normal", "Weak", "Yes"],
[ 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
[ 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
['Overcast', 'Hot', 'Normal', 'Weak', 'Yes"],
['Rain', 'Mild', 'High", "Strong', 'No']

columns= "Outlook", "Temperature', 'Humidity', 'Wind', 'PlayTennis")

def entropy(target_col):
values, counts np.unique(target_col, return counts=True) entropy = sum([-p log2(p) for p in counts/ counts.sum())
return entropy

def info gain(data, split attribute name, target_namez "Playlennis")

total entropy entropy(data)target_name]) vals, counts = np.unique(data[split_attribute name, return counts=True)

def info gain(data, split_attribute_name, target names "PlayTennis"):

total entropy entropy(data[target_name]) vals, counts a np.unique(data split attribute nase), return counts=True)

weighted entropy = sum((counts[i]/ sum(counts)).

entropy(data data split_attribute_name] = vals[i]][target_name])

for i in range(len(vals))

information gain total entropy weighted entropy

return information gain

def ID3(data, original data, features, target_attribute_name="PlayTennis", parent_node_class:None):

if len(np.onique(data[target_attribute_name])) <= 1

return np.unique(data[target_attribute_name])[0]

elif len(data) 0:

return np.unique(original_data[target_attribute_name])[

np.argmax(np.unique(original_data(target_attribute_name], return_counts=True) (1))

elif len(features) 0:

return parent_node_class

else:

parent_node_class = np.unique(data target attribute_name])[

np.argmax(np.unique(data target_attribute name, return countssfrue) 11)

1

item values info gain(data, feature, target attribute name) for feature in features]

best feature_index= np.argmax(item_values)

best feature features best feature index]

tree (best feature: (1)

for value in np.unique(data[best_feature]):

sub data data data[best_feature) == value]

new features features[:best feature index] features best feature_index 11)

subtree= ID3(sub_data, original data, new features, target_attribute_name, parent_node_class)

tree[best_feature][value] = subtree

return tree

features = list(data.columns)

features.remove("PlayTennis")

tree ID3(data, data, features)

import pprint

pprint.pprint(tree)

[Outlook' : ('Overcast': 'Yes',

'Rain': ('Wind": ('Strong': 'No', 'Weak': 'Yes')}, 'Sunny': ('Humidity': {'High': 'No', 'Normal': 'Yes'}}})

def predict(query, tree, default='Yes')

for attr in query:

if attr in tree:

try:

result = tree [attr][query [attr]]
def predict(query, tree, default='Yes');

for attr in query:

if attr in tree:

try:

result = tree[attr][query[attr]]

except:

return default

if isinstance(result, dict):

return predict(query, result)

else:

return result

return default

sample ('Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'

prediction = predict(sample, tree)

print("\nPredicted Output for sample is:", prediction)

