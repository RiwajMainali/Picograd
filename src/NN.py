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

    def NN(lists):
        layersList = []
        for x in lists:
            layersList.append(np.zeros(x))
        # for x in lists:
        #     weights = np.arange(0, shape=())
        return layersList, weights


layersList, weights = Network.NN([2, 3, 5, 7])
