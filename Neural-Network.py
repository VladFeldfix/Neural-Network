import math
import random

<<<<<<< HEAD
# input
x1 = 0.475
x2 = 0.143
=======
class NeuralNetwork:
    def __init__(self, inputs, hidden_layers_qty, hidden_layers_size, outpus):
        self.nn = [[]]
        # first hidden layer
        for _ in range(inputs):
            for _ in range(hidden_layers_size):
                self.nn[0].append(random.uniform(0, 1))
>>>>>>> 917b81338a0432ce3ef9d11c44e033f32450523f

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

<<<<<<< HEAD
# process
n1 = (x1*w1)+b
n2 = (x2*w2)+b
ans = n1+n2
y = 1 / (1 + (math.e ** (-1 * ans)))

# adjust w1, w2, b

# display answer
print(y)
=======
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
>>>>>>> 917b81338a0432ce3ef9d11c44e033f32450523f
