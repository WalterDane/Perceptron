
import numpy
import random
import os

#define constants
learning_rate = 1 #kind of arbitrary
bias = 1 #kind of abitrary
weights = [random.random(), random.random(), random.random()]z

#backpropagation: determines which weight is better to modify
def adjust_weights(error, x1, x2):
    weights[0] += error * x1 * learning_rate
    weights[1] += error * x2 * learning_rate
    weights[2] += error * bias * learning_rate

#activation function
def activate(perceptron_output):
    if perceptron_output > 0:
        perceptron_output = 1
    else:
        perceptron_output = 0
    return perceptron_output

#sigmoid function
def sigmoid(perceptron_output):
    return (1/1+numpy.exp((-perceptron_output)))

#perceptron
def Perceptron(x1, x2, desired_output):
    #get output calculated by perceptron
    perceptron_output = (x1 * weights[0]) + (x2 * weights[1]) + (bias * weights[2])
    perceptron_output = activate(perceptron_output)
    #calculate error
    error = desired_output - perceptron_output
    #adjust weight(s) accordingly
    adjust_weights(error, x1, x2)

#Start of program
#learning phase: train AND
for i in range(100000):
    Perceptron(0, 0, 0)
    Perceptron(0, 1, 0)
    Perceptron(1, 0, 0)
    Perceptron(1, 1, 1)

#testing phase: ask user for input since training is done
x = int(input())
y = int(input())
output = x*weights[0] + y*weights[1] + bias*weights[2]
output = activate(output)
print(x, "AND", y, "is : ", output)