from sklearn.datasets import load_iris
import numpy as np


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

    #ricavo training set e test set
    training_set = matrix[0:50, 0:4]
    y_trainingset = target[0:50]
    test_set = matrix[51:150, 0:4]
    y_testset = target[51:150]
    
    
    #prendo una w qualsiasi
    w = [1,1,1,1,1]
    
    
    print(w)
    
if __name__ == '__main__':
    main()