from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

from Network import Network
from utils import utils
from Dense import Dense
from Activation import Activation

def main():
    iris = load_iris()
    x, y = iris.data, iris.target
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)

    #TODO: inizializare la neural network 
    net = Network()
    net.add(Dense(4,7))
    net.add(Activation(utils.relu, utils.relu_prime))
    net.add(Dense(7,7))
    net.add(Activation(utils.relu, utils.relu_prime))
    net.add(Dense(7,1))
    net.add(Activation(utils.relu, utils.relu_prime))



    #TODO: Fare training 
    net.predict(x_train)

    #TODO: Fare test
    # net.predict(x_test)
    return 

main()