from sklearn.datasets import load_iris
import numpy as np

def binary_cross_entropy(y, h):
    loss_or_cost = -
    return 

def exponent(x,w):
    return np.dot(w,x)

def sigmoid(z):
    res = 1/(1+np.exp(-z))
    return res


def main():
    data = load_iris()
    #data di iris Type Object: Pandas.Matrix
    x_iris = data.data
    #target di iris Type Object: Pandas.Series    
    y_iris = data.target
    
    #trasformo in matrici
    matrix = np.array(x_iris)
    target = np.array(y_iris)
    
    #inserisco prima colonna di tutti 1
    new_column = []
    for i in range(0,150):
        new_column.append(1)
    matrix = np.insert(matrix, 0, new_column, axis=1)

    #target 1,2 positivi 2->1
    # target_12
    #target 0,1 negativi 1->0, 2->1
    # target_01
    #target 0,2 negativi 2->0
    # target_02

    #ricavo training set e test set
    training_set = matrix[0:50, 0:4]
    y_trainingset = target[0:50]
    test_set = matrix[51:150, 0:4]
    y_testset = target[51:150]
    
    
    #prendo una w qualsiasi
    w = [0,0,0,0,0]
    
    
    print(w)
    
if __name__ == '__main__':
    main()