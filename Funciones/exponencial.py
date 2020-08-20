from math import  e

def exponencial(a):
    exp = 1.0
    for i in range(a):
        exp*= e
    return exp
