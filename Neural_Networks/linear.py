import numpy as np

def mean_squared_error(y_true, y_predicted):     
    # Calculating the loss or cost
    cost = np.sum((y_true-y_predicted)**2) / len(y_true)
    return cost

def hypotesis(w,x):
    return np.dot(x,np.transpose(w))
