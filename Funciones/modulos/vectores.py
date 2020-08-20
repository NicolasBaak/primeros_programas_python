# _________________________________________
# Módulo vectores
#  _________________________________________
# Proporciona constrantes y funciones para el cálculo vectorial en 3 dimensiones
#  _________________________________________
# Constantes que exporta:
# vL, vJ, vK: vectores unidad
#
# Funciones que exporta:
# vLeeVector
# sin parámetros
# devuelve un vector leído de teclado que se pide al usuario
#
#  vMuestraVector(v):
# muestra por pantalla el vector v con la notación(x,y,z)
# no devuelve nada
#
# vLongitud()v):
# devuelve la longitud del vector v
#
# vSuma(u, v):
# devuelve el vector resultante de sumar u y v
#
# vProductoEscalar(u, v):
# devuelve el escalar resultante del producto escalar de u por v
#
# vProductorVectorial()u, v):
# devuelve el vector resultante del producto vectorial de u por v
#
# vSonPerpendiculares(u, v):
# devuelve cierto si u y v son perpendiculares, y falso en caso contrario
# ———————————————————————

# Funciones matemáticas utilizadas

from math import  sqrt

# Constantes

vL = [1, 0, 0]
vJ = [0, 1, 0]
vK = [0, 0, 1]

# Funciones entrada/salida


def vLeeVector():
    x = float(input('Componente de x: '))
    y = float(input('Componente de y: '))
    z = float(input('Componente de z: '))
    return [x, y, z]


def vMuestraVector(v):
    print('({0}, {1}, {2})'.format(v[0], v[1], v[2]))

# Funciones de cálculo.


def vLongitud(v):
    return  sqrt(v[0]**2 + v[1]**2 + v[2]**2)


def vSuma(u, v):
    return [u[0]+v[0], u[1]+v[1], u[2]+v[2]]


def vProductoEscalar(u, v):
    return [u[0]*v[0], u[1]*v[1], u[2]*v[2]]


def vProductoVectorial(u, v):
    resultado_x = u[1]*v[2] - u[2]*v[1]
    resultado_y = u[2]*v[0] - u[0]*v[2]
    resultado_z = u[0]*v[1] - u[1]*v[0]
    return  [resultado_x, resultado_y, resultado_z]


# Predicados
def vSonPerpendiculares(u, v):
    return vProductoEscalar(u, v) == 0