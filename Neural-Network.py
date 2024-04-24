import math
import random

class NeuralNetwork:
    def __init__(self, inputs, hidden_layers_qty, hidden_layers_size, outpus):
        self.nn = [[]]
        # first hidden layer
        for _ in range(inputs):
            for _ in range(hidden_layers_size):
                self.nn[0].append(random.uniform(0, 1))

        # rest of hidden layers
        for hls in range(hidden_layers_qty):
            self.nn.append([])
            for _ in range(hidden_layers_size):
                for _ in range(hidden_layers_size):
                    self.nn[hls+1].append(random.uniform(0, 1))

        # results
        self.nn.append([])
        for _ in outpus:
            self.nn[-1].append(random.uniform(0, 1))
        self.outpus = outpus
        #print(self.nn)

    def get_labeled_data(self, data, lbl):
        result = data
        for layer in self.nn:
            result = self.matrix_multiplication(result, layer)
        
        # what is the result
        #print(result)
        #print(result.index(max(result)))
        chosen_result_index = result.index(max(result))
        print(self.outpus[chosen_result_index])
            
    def matrix_multiplication(self, A, B):
        #print(A)
        #print(B)
        result = []
        for b in B:
            ans = 0
            for a in A:
                ans += a*b
            y = 1 / (1 + (math.e ** (-1 * ans)))
            result.append(y)
        #print(result)
        return result

nn = NeuralNetwork(4,5,3,['square','circe'])
nn.get_labeled_data([0.1,0.2,0.3],'square')