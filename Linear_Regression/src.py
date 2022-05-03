from sklearn.datasets import load_iris
import numpy as np

ALPHA = 0.01

def normal_equations(matrix, target):
    trans = np.transpose(matrix)
    w = np.dot((np.dot((np.linalg.inv(np.dot(trans, matrix))), trans)), target)
    return w

def stocastich_gradient_descendendt(w, y, set):
    for i in range(0,len(set)):
        for j in range(0,len(set[i])):    
            w[j] -= ALPHA*(np.dot(w, set[i]) - y[i])*set[i][j]
    return  


def main():
    data = load_iris()
    #data di iris Type Object: Pandas.Matrix
    x_iris = data.data
    #target di iris Type Object: Pandas.Series    
    y_iris = data.target
    
    #trasformo in matrici
    matrix = np.array(x_iris)
    target = np.array(y_iris)

    #ricavo training set e test set
    training_set = matrix[0:50, 0:4]
    y_trainingset = target[0:50]
    test_set = matrix[51:150, 0:4]
    y_testset = target[51:150]

    #calcolo il vettore w ottimo 
    w_star = normal_equations(matrix, target)
    #prendo una w qualsiasi
    w = [1,1,1,1]
    
    stocastich_gradient_descendendt(w,target, matrix)
    print(w_star)
    print(w)

if __name__ == '__main__':
    main()