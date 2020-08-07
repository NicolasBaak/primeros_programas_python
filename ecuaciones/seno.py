from turtle import  Screen, Turtle
from math import sin, cos, pi

#Vamos a usar el módulo de la tortuga para representar gráficamente funciones matemáticas.
#Utilizaremos la función seno, pero trataremos de que nuestro programa sea fácilmente modificable para utilizar las que deseemos

#Hagamos que el usuario pueda introducir el intervalo de valores de x que desea examinar, así
#como el número de puntos que desee representar

x1 = float(input('Dime el límite inferior del intervalo: '))
x2 = float(input('Dime el límite superior del intervalo: '))
puntos = int(input('Dime cúantos puntos he de mostrar: '))

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(x1, -1, x2, 1)

x = x1
dx = (x2 - x1) / puntos
tortuga = Turtle()
tortuga.penup()
tortuga.goto(x, sin(x))
tortuga.pendown()
tortuga.color('red')
while x <= x2:
    tortuga.goto(x, sin(x))
    x +=dx
x = x1
tortuga.penup()
tortuga.goto(x, cos(x))
tortuga.color('blue')
tortuga.pendown()
while x <= x2:
    tortuga.goto(x, cos(x))
    x +=dx
pantalla.exitonclick()