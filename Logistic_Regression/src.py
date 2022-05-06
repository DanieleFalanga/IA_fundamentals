from __future__ import print_function
from sklearn.datasets import load_iris
import numpy as np

ALPHA = 0.001 

def binary_cross_entropy(y,theta):
    cost = 0
    for i in range(0,len(y)):
        cost += (-(y[i]*np.log10(theta[i]) + (1-y[i])*np.log10(1-theta[i])))
    return cost

def Logistic_Regression(w,y,x):
    #scansiono colonne di x
    previus_cost = None
    exp = exponent(x,w)
    hyp = theta(exp)
    while(binary_cross_entropy(y,hyp) > 0.001):
        current_cost = binary_cross_entropy(y,hyp)
        # print(current_cost)
        if previus_cost and current_cost > previus_cost:
            print("Loss Totale: ", previus_cost)
            break
        previus_cost = current_cost
        for j in range(0,len(x[0])):
            # scansiono le righe di x
            for i in range(0,len(x)):
                w[j] += ALPHA*(y[i]-hyp[i])*x[i][j]
        exp = exponent(x,w)
        hyp = theta(exp)
        
    return previus_cost


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
    target_12 = target
    for i in range(0,len(target)):
        if target_12[i] == 2:
            target_12[i] = 1
    
    #target 0,1 negativi 1->0, 2->1
    target_01 = target
    for i in range(0,len(target)):
        if target_01[i] == 1:
            target_01[i] = 0
        elif target_01[i] == 2:
            target_01[i] = 1
        
    
    #target 0,2 negativi 2->0
    target_02 = target
    for i in range(0,len(target)):
        if target_02[i] == 2:
            target_02[i] = 0

    
    #prendo una w qualsiasi
    w = [1,1,1,1,1]
    
    print(w)
    print("#################LOGISTIC REGRESSION 1 #################")
    print("target 1,2 positivi 2->1")
    print("")
    print("Vettore W di partenza: ", w)
    print("")
    loss = Logistic_Regression(w,target_12, matrix)
    print("Vettore W dopo Logistic Regression: \n", w)
    print("Loss: ", loss)

    print("#################LOGISTIC REGRESSION 2 #################")
    w = [1,1,1,1,1]
    print("target 0,1 negativi 1->0, 2->1")
    print("")
    print("Vettore W di partenza: ", w)
    print("")
    loss = Logistic_Regression(w,target_01, matrix)
    print("Vettore W dopo Logistic Regression:\n", w)
    print("Loss: ", loss)

    print("#################LOGISTIC REGRESSION 3 #################")
    w = [1,1,1,1,1]
    print("target 0,2 negativi 2->0")
    print("")
    print("Vettore W di partenza: ", w)
    print("")
    loss = Logistic_Regression(w,target_02, matrix)
    print("Vettore W dopo Logistic Regression:\n", w)
    print("Loss: ", loss)
    


if __name__ == '__main__':
    main()