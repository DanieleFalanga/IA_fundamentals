from Layer import Layer
import numpy as np 

class Dense(Layer):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.weights = np.random.rand(output_size, input_size)
        self.bias = np.random.rand(output_size, 1)

    def forward(self, input):
        self.input = input
        output = np.dot(self.weights, self.input) + self.bias
        return output
    
    def backward(self, output_gradient, learning_rate):
        weights_gradients = np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate*weights_gradients
        self.bias -= learning_rate*output_gradient
        return np.dot(self.weights.T, output_gradient)