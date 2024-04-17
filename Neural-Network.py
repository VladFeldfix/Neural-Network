import math


# weights
w1 = 0.5
w2 = 0.5

# bios
b = 0.5

def activation_function(x1, x2):
    n1 = (x1*w1)+b
    n2 = (x2*w2)+b
    ans = n1+n2
    return 1 / (1 + (math.e ** (-1 * ans)))

def learn(data, lbl):

    pass

learn(0.475, 0.143)