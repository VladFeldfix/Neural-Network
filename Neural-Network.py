import math

# inputs
x1 = 1.745
x2 = 2.547

# weights
w1 = 0.5
w2 = 0.5

# bios
b = 0.5

# data lbl
GOAL = 1

# activation_function
n1 = (x1*w1)+b
n2 = (x2*w2)+b
ans = n1+n2
y = 1 / (1 + (math.e ** (-1 * ans)))

# LEARNING
# calculate derivative
# w1
loss_y_derivative = 2*(y - GOAL)
y_ans_derivative = ans *  math.e**-ans / (1 + math.e**-ans)**2
loss_ans_derivative = loss_y_derivative * y_ans_derivative
ans_n1_derivative = 1 # why one?
loss_n1_derivative = loss_ans_derivative * ans_n1_derivative
n1_w1_derivative = x1
loss_w1_derivative = loss_n1_derivative * n1_w1_derivative
w1_derivative = loss_w1_derivative

# w2
loss_y_derivative = 2*(y - GOAL)
y_ans_derivative = ans *  math.e**-ans / (1 + math.e**-ans)**2
loss_ans_derivative = loss_y_derivative * y_ans_derivative
ans_n2_derivative = 1 # why one?
loss_n2_derivative = loss_ans_derivative * ans_n2_derivative
n1_w2_derivative = x2
loss_w2_derivative = loss_n2_derivative * n1_w2_derivative
w2_derivative = loss_w2_derivative

# gradient descent
# computes d(loss)/d(w1), meaning the derivative of the loss function with respect to w1
# how should I compute d(loss)/d(w1)?  With the chain rule: 
# d(loss)/d(w1) = d(loss)/dy • dy/d(ans) • d(ans)/d(n1) • d(n1)/d(w1)
LR = 0.001 # step size?
w1 -= LR*w1_derivative
w2 -= LR*w2_derivative

# display answer
print(y)
print("Old w1 = 0.5")
print("Old w2 = 0.5")
print("New w1 = "+str(w1))
print("New w2 = "+str(w2))
print("What about the bios?")