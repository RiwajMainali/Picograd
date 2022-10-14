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

    # if a neuron isn't needed in a layer, put it as zero which is why, max(layers) is used.
    def NN(layers, dim=2):

        layersList = np.zeros((max(layers), len(layers)), dtype=float)
        weights = []
        return layersList, weights


layers, weights = Network.NN([2, 4, 5])
print(layers)
