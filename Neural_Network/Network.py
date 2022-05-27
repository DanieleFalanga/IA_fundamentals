import numpy as np
class Network():
    def __init__(self):
        self.layers = []
        #self.loss = loss
        #self.loss_prime = loss_prime

    def add(self, layer):
        self.layers.append(layer)


    def MSE(self, y_pred, y_true):
        return np.mean(np.power(y_true - y_pred, 2))

    def MSE_prime(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / y_pred.size

    def predict(self, input):
        output = input
        for layer in self.layers:
            output = layer.forward(output)
        return output

    def train(self, x_train, y_train, epochs = 1000, learning_rate = 0.01, verbose = True):
        for e in range(epochs):
            error = 0
            for x, y in zip(x_train, y_train):
                # forward
                output = self.predict(x)

                # error
                error += self.MSE(y, output)

                # backward
                grad = self.MSE_prime(y, output)
                for layer in reversed(self.layers):
                    grad = layer.backward(grad, learning_rate)

            error /= len(x_train)
            if verbose:
                print(f"{e + 1}/{epochs}, error={error}")
