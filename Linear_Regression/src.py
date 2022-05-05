from sklearn.datasets import load_iris
import numpy as np
from sklearn.metrics import mean_absolute_error

ALPHA = 0.0001  
CONVERGENCE = 0.001


#funzione per trovare w* ottimo, È SOLO DI PROVA
def normal_equations(matrix, target):
    trans = np.transpose(matrix)
    w = np.dot((np.dot((np.linalg.inv(np.dot(trans, matrix))), trans)), target)
    return w

def hypotesis(w,x):
    w = np.transpose(w)
    h = np.dot(x,w)
    return h 

def bias(y_i, hyp_i):
    return (y_i-hyp_i)

def mean_squared_error(y_true, y_predicted):     
    # Calculating the loss or cost
    cost = np.sum((y_true-y_predicted)**2) / len(y_true)
    return cost

def stochastich_gradient_descendent(w,y,x):
    #scansiono colonne di x
    previus_cost = None
    while(True):
        hyp = hypotesis(w,x)
        current_cost = round(mean_squared_error(y,hyp),4)
        print(current_cost)
        if previus_cost and current_cost > previus_cost:
            print("Loss Totale: ", previus_cost)
            break
        previus_cost = current_cost
        for j in range(0,len(x[0])):
            # scansiono le righe di x
            for i in range(0,len(x)):
                w[j] += ALPHA*(bias(y[i],hyp[i]))*x[i][j]
        
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
 
    #calcolo il vettore w ottimo 
    w_star = normal_equations(matrix, target)
    #prendo una w qualsiasi
    w = [3,2,4,6,1]
    
    stochastich_gradient_descendent(w,target, matrix)
    print(w_star)
    print(w)

if __name__ == '__main__':
    main()