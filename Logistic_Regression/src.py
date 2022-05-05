from sklearn.datasets import load_iris
import numpy as np

ALPHA = 0.001 

def binary_cross_entropy(y,theta):
    cost = 0
    for i in range(0,len(y)):
        cost += (-(y[i]*np.log(theta[i]) + (1-y[i])*np.log(1-theta[i])))
    return cost

def Logistic_Regression(w,y,x):
    #scansiono colonne di x
    previus_cost = None
    while(True):
        exp = exponent(x,w)
        hyp = theta(exp)
        current_cost = binary_cross_entropy(y,hyp)
        print(current_cost)
        if previus_cost and current_cost > previus_cost:
            print("Loss Totale: ", previus_cost)
            break
        previus_cost = current_cost
        for j in range(0,len(x[0])):
            # scansiono le righe di x
            for i in range(0,len(x)):
                w[j] += ALPHA*(y[i]-hyp[i])*x[i][j]
        
    return 


def exponent(x,w): 
    return np.dot(x,np.transpose(w))

def theta(z):
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
    training_set = matrix[0:70, 0:5]
    y_trainingset = target[0:70]
    test_set = matrix[51:150, 0:4]
    y_testset = target[51:150]
    
    
    #prendo una w qualsiasi
    w = [1,1,1,1,1]
    Logistic_Regression(w,y_trainingset, training_set)
    
    print(w)
    


if __name__ == '__main__':
    main()