from asyncio.windows_events import NULL
import numpy as np
import math
activationFunctions = ['reLU', 'sigmoid', 'LreLU']


class NN:
    def reLU(number):
        return max(0.0, number)

    def LreLU(number):
        if number > 0:
            return number
        else:
            return 0.01*number

    def sigmoid(number):
        return (1/(1+math.exp(-number)))

    def __init__(self, layers, weightsDim=None):
        '''
            if a neuron isn't needed in a layer, put it as zero which is why, max(layers) is used.
            weightsDim will will accept list of dimensions. User will be responsible to match it with layers to make sure dot product is possible
        '''
        self.layers = np.ones((max(layers), len(layers)), dtype=float)

        if weightsDim is not None:
            self.weights = np.ones((max(weightsDim), len(weightsDim)))

        else:
            self.weights = np.ones((max(layers), len(layers)), dtype=float)

        self.bias = np.ones(len(layers))
        return None


basicNN = NN([2, 4, 5])
print(basicNN.layers, basicNN.weights, basicNN.bias)
