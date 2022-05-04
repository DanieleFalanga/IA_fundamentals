from sklearn.datasets import load_iris
import numpy as np

ALPHA = 0.01
CONVERGENCE = 0.00000000001


#funzione per trovare w* ottimo, È SOLO DI PROVA
def normal_equations(matrix, target):
    trans = np.transpose(matrix)
    w = np.dot((np.dot((np.linalg.inv(np.dot(trans, matrix))), trans)), target)
    return w

def hypotesis(w,x):
    w = np.transpose(w)
    h = np.dot(x,w)
    return h 

def loss(y_i, hyp_i):
    return (y_i-hyp_i)

def stochastich_gradient_descendent(w,y,x):
    converge = False
    #scansiono colonne di x
    while(converge == False):
        hyp = hypotesis(w,x)
        for j in range(0,len(x[0])):
            # scansiono le righe di x
            for i in range(0,len(x)-100):
                #print(i,j)
                if (abs(loss(y[i],hyp[i])) <= CONVERGENCE):
                    print("Sono nell' if")
                    converge = True
                    continue
                print("Aggiorno w[j]")
                w[j] += ALPHA*(loss(y[i],hyp[i]))*x[i][j]
                converge = False
        
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
    w = [1,1,1,1,1]
    
    # stochastich_gradient_descendent(w,target, matrix)
    print(w_star)
    print(w)
    #print(matrix)

if __name__ == '__main__':
    main()