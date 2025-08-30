import numpy as np

class NeuralNetwork:
    # Initialization
    def __init__(self,layers=[3,5,2]):
        self.layers = layers
        self.biases = [np.zeros((layers[i],1)) for i in range(len(layers))]
        self.weights = [np.random.randn(layers[i],layers[i-1])*0.1 for i in range(1,len(layers))]
    # Activation
    def __activation__(self,data,method):
        if method == "tanh":
            extra = np.tanh(data)
        elif method == "softmax":
            x = np.exp(data-np.max(data))
            extra = x/x.sum(axis=0)
        return extra
    # Cross Entropy Loss - probability
    def cross_entropy_loss(pred,true):
        return -np.sum(true*np.log(pred+1e-9))
    # Mean Squared Error - Continuous
    def mse_loss(pred,true):
        return np.mean((pred-true)**2)
    # Fitness - How good it is.
    def fitness(pred,true):
        return 1/(1+mse_loss(pred,true))
    # Replace all current values.
    def regenerate(self,layers=[3,5,2]):
        self.layers = layers
        self.biases = [np.zeros((layers[i],1)) for i in range(len(layers))]
        self.weights = [np.random.randn(layers[i],layers[i-1])*0.1 for i in range(1,len(layers))]
    # Mutate - Change values.
    def mutate(self,rate=0.1,str=0.5):
        for i in range(len(self.weights)):
            mutation_mask = np.random.rand(*self.weights[i].shape) < rate
            self.weights[i] += mutation_mask * np.random.randn(*self.weights[i].shape) * strength
            mutation_mask = np.random.rand(*self.biases[i].shape) < rate
            self.biases[i] += mutation_mask * np.random.randn(*self.biases[i].shape) * strength
    # Forward - Get output from the AI
    def forward(self,data,method="tanh"):
        self.method, self.inputs = method, data
        a = data
        for w,b in zip(self.weights,self.biases):
            extra = np.dot(w,a)+b
            a = self.__activation__(extra,method)
        self.outputs = a
        return a