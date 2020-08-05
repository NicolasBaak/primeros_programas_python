from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

# Diseña un programa que dibuje un triángulo equilátero con la tortuga.
# El trazo del triángulo debe tener un grosor de 10 píxeles.

tortuga = Turtle()
tortuga.pensize(10)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)

# No uses los métodos left o right.
tortuga.setheading(0)
tortuga.pensize(2)
tortuga.color('white')
tortuga.forward(100)
tortuga.setheading(120)
tortuga.forward(100)
tortuga.setheading(240)
tortuga.forward(100)

pantalla.exitonclick()