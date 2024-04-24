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
        
        #print(self.nn)

    def get_labeled_data(self, data, lbl):
        result = data
        for layer in self.nn:
            result = self.matrix_multiplication(result, layer)
            
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
        print(result)
        return result
nn = NeuralNetwork(4,5,3,['square','circe'])
nn.get_labeled_data([0.1,0.2,0.3],'square')
"""
class NeuralNetwork:
    def __init__(self, inputs, hidden_layers_qty, hidden_layers_size, outpus):
        self.nn = [[]]
        # first hidden layer
        for hls in range(hidden_layers_size):
            self.nn[0].append([])
            for _ in range(inputs):
                self.nn[0][hls].append(0.5)
        
        # rest of hidden layers
        for hlq in range(hidden_layers_qty):
            self.nn.append([])
            for hls in range(hidden_layers_size):
                self.nn[hlq+1].append([])
                for _ in range(hidden_layers_size):
                    self.nn[hlq+1][hls].append(0.4)
    
    def get_labeled_data(self, labeled_data):
        # labeled_data = [
        #                   [[list, of, nodes, to, process, ...], lbl],
        #                   [[list, of, nodes, to, process, ...], lbl],
        #                   ...
        #                ]
        # go over each data node
        for data in labeled_data:
            nodes = data[0]
            lbl = data[1]
            #print(nodes)
            # [0.254, 1.251, 2.251]
            # [0.245, 1.214, 1.541]
            self.matrix_multiplication(nodes,self.nn[0])
    
    def matrix_multiplication(self, A, B):
        result = []
        for bb in B:
            for b in bb:
                for a in A:
                  result.append(a*b)
        print(result)
        
nn = NeuralNetwork(4,5,3,['square','circe'])
nn.get_labeled_data([[[0.1,0.2,0.3],'square'],[[0.4,0.5,0.6],'circe']])

"""