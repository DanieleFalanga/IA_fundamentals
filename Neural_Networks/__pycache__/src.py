from sklearn.datasets import load_iris
import numpy as np
from network import network
from layer import layer

def main():
    data = load_iris()
    x_iris = data.data
    y_iris = data.target
    
    matrix = np.array(x_iris)
    target = np.array(y_iris)
    
    #inizializzo la rete neurale

    net = network()

    #aggiungo i due layer di 7 neuroni ciascuno
    lay1 = layer(4,7)
    lay2 = layer(7,1)
    net.add(lay1)
    net.add(lay2)


    output = net.fit(matrix, target, 1000, 0.01)
    print(output)
    return 


main()
