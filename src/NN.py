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

    def NN(lists, activationFunction):

        dataType = object
        arr = np.zeros(shape=(len(lists)), dtype=dataType)
        for x in range(0, len(lists)):
            arr[x] = np.zeros(shape=lists[x], dtype=dataType)
        return arr
