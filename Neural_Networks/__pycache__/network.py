import numpy as np
from more_itertools import sample


class network():
    layers = []
    
    def __init__(self) -> None:
        pass

    def add(self, layer):
        self.layers.append(layer)
    
    def predict(self, input):
        result = None

        output = input
        for layer in self.layers:
            output = layer.forward(output)
        result = output
        
        return result

    def mse (self, y_true, y_predicted):
        cost = np.sum((y_true-y_predicted)**2) / len(y_true)
        return cost

    def mse_prime(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / y_pred.size

    def fit(self,x_train,y_train,epochs, learning_rate):
        output = []
        
        #faccio stochastich dando come input alla rete la singola riga
        #restituendo l'output corrispondente
        
        for i in range(0,len(x_train)):
            for i in range(0,epochs):    #faccio epochs iterazioni per la singola riga
                y_pred = self.predict(x_train[i])
                loss = self.mse (y_train[i], y_pred)
                if loss < 0.03: #se la loss è abbastanza bassa appendo al vettore di output
                    output.append(y_pred)
                    break
                
                #se sto qua la loss è ancora alta, devo fare backpropagation

            
        
        return output

