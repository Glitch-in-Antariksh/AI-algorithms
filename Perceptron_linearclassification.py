import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [2, 3],
    [4, 5],
    [1, 1],
    [6, 7],
    [2, 1],
    [7, 8]
])

y = np.array([1, 1, -1, 1, -1, 1])


class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation(self, x):
        return np.where(x >= 0, 1, -1)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = self.activation(linear_output)

                if y[i] != y_pred:
                    self.weights += self.lr * y[i] * X[i]
                    self.bias += self.lr * y[i]

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation(linear_output)


# 🚀 NOW run stuff here (outside class)
model = Perceptron(lr=0.1, epochs=20)
model.fit(X, y)

predictions = model.predict(X)
print("Predictions:", predictions)


def plot_decision_boundary(X, y, model):
    plt.scatter(X[:, 0], X[:, 1], c=y)

    x0 = np.linspace(0, 8, 100)
    x1 = -(model.weights[0] * x0 + model.bias) / model.weights[1]

    plt.plot(x0, x1)
    plt.show()


plot_decision_boundary(X, y, model)

