import numpy as np
def sigmoid(x):

return 1/(1+ nпрекр(-))

def sigmoid derivative(x)

return x * (1-x)

def binary cross entropy(y true, y_pred):

return -np.mean(y true np.log(y_pred 3-7)  * (1 y true) np.log (1- y_pred + te-7))

def train_neural_network(X, y, epochs=10000, 1:8.1);

input dim X.shape[1]

weights np.random.uniform(size=(input dim, 1)) bias np.random.unifore(sizes(1))

for epoch in range(epochs):

Linear output = np.dot(X, weights) bias predictions sigmoid(linear output)

loss binary cross entropy(y, predictions)

error= predictions - y

d_pred = error * sigmoid_derivative(predictions)

weights Ir np.dot (X.T, d_pred) bias np.sum(d pred)

if epochs 10000:

print("Epoch epoch), Lass: (Inss:.4f)")
return weights, bias

def predict(X, weights, bias):
return sigmoidinp-dot(X, weights) + bias) >= 0.5


(X) = np.array([[0,0], [0,1], [1,0], [1,1]])

logic_gates = {

"AND" np.array([[0], [0], [0], [1]]),

"OR": np.array([[9], [1], [1], [1]1),

"NANID":np.array([[1], [1], [1], [0]]),

"NOR": np.array([[1], [0], [e], [e]]),

"XOR": np.array([[8], [1], [1], [0]]),
}
for gate_name, y in logic gates.items():

print (f"\nTraining for gate name) gate:")

weights, bias train_neural_network(X, y, epochs=10000, 1r=0.1)

predictions predict(X, weights, bias).astype(int)

print (f"Predictions for (gate_name] gate:\n[predictions.reshape(-1)}")

