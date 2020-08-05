from turtle import Screen, Turtle
'''
"setup" de pantalla, fija el ancho (425 píxeles) y alto (225 píxeles) de la ventana. 
"screensize()", que fija el tamaño de la superficie de dibujo (400 píxeles de ancho y 200 de alto). 
la ventana contiene algunos elementos decorativos que necesitan su propio espacio.
'''
pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
'''
El método left hace que la tortuga gire hacia la izquierda tantos grados como se indique en
el único argumento del método
'''
tortuga = Turtle()
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
'''
El método penup, sin argumentos, levanta el lápiz, y el método pendown, también sin argumentos, 
lo vuelve a apoyar en la superficie de dibujo. Usamos ambos métodos para dibujar dos cuadrados no conectados
'''
tortuga.penup()
tortuga.right(90)
tortuga.forward(100)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()