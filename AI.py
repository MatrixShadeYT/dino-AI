import numpy as np

default_layer = 3
score = 0

def create_network(inputs=default_layer,hidden=[1,default_layer],outputs=default_layer):
    network = [np.random.randn(hidden[1],hidden[1]) for i in range(hidden[0]-1)]
    network.insert(0,np.random.randn(inputs,hidden[1]))
    network.append(np.random.randn(hidden[1],outputs))
    return network

def mutate(network,rate=0.1):
    for key in range(len(network)):
        network[key] += np.random.randn(*network[key].shape) * rate
    return network

def forward(network,x):
    h = np.tanh(np.dot(x, network[0]))
    out = np.dot(h, network[len(network)-1])
    return np.argmax(out)

def calculate(network,data):
    return forward(network,data)