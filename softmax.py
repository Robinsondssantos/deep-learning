import math
import numpy as np

def softmax(z, x):
    return np.exp(z)/sum(np.exp(z))

def simple_softmax(l=[]):
    exp_list = []
    final_list = []
    for x in l:
        exp_list.append(math.e**x)
    total = sum(exp_list)
    for i in exp_list:
        final_list.append(i/total)
    return final_list

def simple_softmax2(l=[]):
    exp_list = [math.e**x for x in l]
    total = sum(exp_list)
    return [i / total for i in exp_list]