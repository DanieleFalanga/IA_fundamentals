from sklearn.datasets import load_iris
import numpy as np

ALPHA = 0.0001

#funzione per trovare w* ottimo, È SOLO DI PROVA
def normal_equations(matrix, target):
    trans = np.transpose(matrix)
    w = np.dot((np.dot((np.linalg.inv(np.dot(trans, matrix))), trans)), target)
    return w

def stocastich_gradient_descendendt(w, y, x):
    old_w = w
    for i in range(0,len(x)):
        for j in range(0,len(x[i])):    
            w[j] -= ALPHA*(np.dot(old_w, x[i]) - y[i])*x[i][j]
    w = old_w
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
    
    
    #calcolo il vettore w ottimo 
    w_star = normal_equations(matrix, target)
    #prendo una w qualsiasi
    w = [0,0,0,0,0]
    
    stocastich_gradient_descendendt(w,target, matrix)
    print(w_star)
    print(w)

if __name__ == '__main__':
    main()