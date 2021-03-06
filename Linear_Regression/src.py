from sklearn.datasets import load_iris
import numpy as np
from sklearn.metrics import mean_absolute_error

ALPHA = 0.0001  


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
        current_cost = mean_squared_error(y,hyp)
        #print(current_cost)
        if previus_cost and current_cost > previus_cost:
            break
        previus_cost = current_cost
        for j in range(0,len(x[0])):
            # scansiono le righe di x
            for i in range(0,len(x)):
                w[j] += ALPHA*(bias(y[i],hyp[i]))*x[i][j]
        
    return previus_cost
        
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
    

    print("#################LINEAR REGRESSION#################")
    print("Esecuzione molto lenta, per vedere l'esecuzione, decommentare la print del costo nella funzione stochastich_gradient_descendent")
    print("")
    print("Vettore W di partenza: \n", w,)
    print("")
    print("Vettore W* calcolato tramite Normal Equations: \n", w_star)
    print("")
    loss = stochastich_gradient_descendent(w,target, matrix)
    print("Vettore W calcolato dalla stochastich_gradient_descendent tramite MSE: \n", w)
    print("")
    print("Loss: ", loss)

if __name__ == '__main__':
    main()