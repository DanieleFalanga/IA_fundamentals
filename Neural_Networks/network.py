import numpy as np

class network:
    def __init__(self):
        self.layers = []
        self.loss = None
    
    def forward_propagation(x,w,b):
        hidden_layer_input = np.dot(x,w) + b

        hidden_layer_activations =  