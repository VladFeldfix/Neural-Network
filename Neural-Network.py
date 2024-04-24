import math

# input
x1 = 0.475
x2 = 0.143

# weights
w1 = 0.5
w2 = 0.5

# bios
b = 0.5

# process
n1 = (x1*w1)+b
n2 = (x2*w2)+b
ans = n1+n2
y = 1 / (1 + (math.e ** (-1 * ans)))

# adjust w1, w2, b

# display answer
print(y)