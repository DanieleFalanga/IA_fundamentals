import numpy as np

class layer():
    def __init__(self, n_input, n_neurons):
        self.weights = np.random.rand(n_input, n_neurons)
        self.bias = np.random.rand(1,n_neurons) 


    def forward(self, input):
        output = np.dot(self.weights, input) + self.bias
        return np.maximum(0,output)

    def backprop():
        
        pass
