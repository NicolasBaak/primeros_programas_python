from math import sin, pi


def xsin(x):
    return x * sin(x)


def cuadrado(x):
    return x ** 2


def raiz_cubica(x):
    return x **(1/3)


def area_circulo(r):
    return pi*(r**2)


def FarenheitToCelcius(x):
    return (x-32)*(5/9)


def CelciusToFarenheit(x):
    return (x+32)/(5/9)


print(cuadrado(2))
a = 1 + cuadrado(3)
print(cuadrado(a*3))