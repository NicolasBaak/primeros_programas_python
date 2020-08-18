#Definamos una función que, dados los tres lados de un triángulo,
#devuelva el valor de su área.
from math import sqrt, asin, pi


def area_triangulo(a, b, c):
    s = (a+b+c)/2
    argumento = s*(s-a)*(s-b)*(s-c)
    if argumento >= 0:
        return sqrt(argumento)
    else:
        return 0


def angulo_alfa(a, b, c):
    s = area_triangulo(a, b, c)
    if b*c <= 0 and 2*s != 0:
        return 0
    else:
        return 180 / pi * asin(2*s/(b*c))


def menu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print('1) Calcular area del triangulo')
        print('2) Calcular angulo opuesto al primer lado')
        opcion = int(input('Escoge una opción: '))
    return opcion


lado1 = float(input('Dame lado a: '))
lado2 = float(input('Dame lado b: '))
lado3 = float(input('Dame lado c: '))

s = menu()

if s == 1:
    resultado = area_triangulo(lado1, lado2, lado3)
else:
    resultado = angulo_alfa(lado1, lado2, lado3)

print('Escogiste la opcion',s)
print('El resultado es: ', resultado)