from math import  sqrt

x = -1
while x < 0:
    x = float(input('Introduce un número positivo: '))

print('La raiz cuadrad de {0} es {1}'.format(x, sqrt(x)))