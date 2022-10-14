from asyncio.windows_events import NULL
import numpy as np
import math
activationFunctions = ['reLU', 'sigmoid', 'LreLU']


class Network:
    def reLU(number):
        return max(0.0, number)

    def LreLU(number):
        if number > 0:
            return number
        else:
            return 0.01*number

    def sigmoid(number):
        return (1/(1+math.exp(-number)))

    def NN(layers, weightsDim=None):
        '''
            if a neuron isn't needed in a layer, put it as zero which is why, max(layers) is used.
            weightsDim will will accept list of dimensions. User will be responsible to match it with layers to make sure dot product is possible
        '''
        weights = []
        layersList = np.zeros((max(layers), len(layers)), dtype=float)

        if weightsDim is not None:
            weights = np.zeros((max(weightsDim), len(weightsDim)))

        else:
            weights = np.zeros((max(layers), len(layers)), dtype=float)

        return layersList, weights, weightsDim


# layers, weights, weightsDim = Network.NN([2, 4, 5], [2, 1])
