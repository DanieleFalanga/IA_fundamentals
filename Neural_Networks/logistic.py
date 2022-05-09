import numpy as np


def binary_cross_entropy(y,sigmoid):
    cost = 0
    for i in range(0,len(y)):
        cost += (-(y[i]*np.log10(sigmoid[i]) + (1-y[i])*np.log10(1-sigmoid[i])))
    return cost

def sigmoid(x,w):
    exp = np.dot(x,np.transpose(w))
    res = 1/(1+np.exp(-z))
    return res
