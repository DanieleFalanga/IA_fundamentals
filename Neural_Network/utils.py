import numpy as np 

class utils():
    def relu(x):
        return np.maximum(x, 0)

    def relu_prime(x):
        return np.array(x > 0).astype('int')

    #def MSE(self, y_pred, y_true):
    #    return np.mean(np.power(y_true - y_pred, 2))
#
    #def MSE_prime(self, y_true, y_pred):
    #    return 2 * (y_pred - y_true) / y_pred.size