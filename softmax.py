import numpy as np

def softmax(z, x):
    return np.exp(z)/sum(np.exp(z))

def simple_softmax(l=[]):
    total = 0
    for x in range(l):
        total += x**2
    return total**2