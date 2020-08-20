from turtle import Screen, Turtle
from math import sqrt


def koch(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        koch(tortuga, longitud/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)
        tortuga.right(120)
        koch(tortuga, longitud/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)


def copo(tortuga, longitud, nivel):
    koch(tortuga, longitud, nivel)
    tortuga.right(120)
    koch(tortuga, longitud, nivel)
    tortuga.right(120)
    koch(tortuga, longitud, nivel)

def dragon(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        tortuga.right(45)
        dragon(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.left(90)
        nogard(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.right(45)


def nogard(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        tortuga.left(45)
        dragon(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.right(90)
        nogard(tortuga, longitud/sqrt(2), nivel-1)
        tortuga.left(45)



# Programa principal
pantalla = Screen()
pantalla.setup(500, 500)
pantalla.screensize(500, 500)
pantalla.setworldcoordinates(0, -350, 500, 150)

tortuga = Turtle()
tortuga.speed(0)
dragon(tortuga, 400, 10)
pantalla.exitonclick()