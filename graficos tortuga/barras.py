from turtle import Screen, Turtle

# Calificaciones ingresadas predefinidas
suspensos = int(input("Ingresa el numero de suspensos: "))
aprobados = int(input("Ingresa el numero de aprobados: "))
notables = int(input("Ingresa el numero de notables: "))
sobresalientes = int(input("Ingresa el numero de sobresalientes: "))

total = suspensos + aprobados + notables + sobresalientes

suspensos = (suspensos * 100) / total
aprobados = (aprobados * 100) / total
notables = (notables * 100) / total
sobresalientes = (sobresalientes * 100) / total

#Inicialización
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

pantalla.setworldcoordinates(-50, -50, 350, 250)

#Esconder la tortuga
tortuga.hideturtle()

total = 20
tamaCuadro = 50
numCuadro = 1
espacio = 15
#Dibujar primer cuadro suspensos
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(suspensos * 100 / total)
tortuga.left(90)
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(suspensos * 100 / total)
#Escribir texto del suspenso
tortuga.penup()
tortuga.forward(espacio)
tortuga.pendown()
tortuga.write('suspensos')
tortuga.penup()
tortuga.backward(espacio)

# Escribir el porcentaje sobre el cuadro
tortuga.backward((suspensos* 100 / total))
tortuga.setheading(0)
tortuga.forward(tamaCuadro/2)
tortuga.write('{0:.1f}%'.format(suspensos))
tortuga.backward(tamaCuadro/2)
tortuga.setheading(270)
tortuga.forward(suspensos * 100 / total)
tortuga.setheading(0)

#mover la tortuga a otro  rectangulo
tortuga.setheading(0)
tortuga.forward(tamaCuadro*numCuadro + 20)
tortuga.pendown()
++numCuadro

#Dibujar primer cuadro aprobados
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(aprobados * 100 / total)
tortuga.left(90)
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(aprobados * 100 / total)
#Escribir texto de aprobados
tortuga.penup()
tortuga.forward(espacio)
tortuga.pendown()
tortuga.write('aprobados')
tortuga.penup()
tortuga.backward(espacio)

# Escribir el porcentaje sobre el cuadro
tortuga.backward((aprobados* 100 / total))
tortuga.setheading(0)
tortuga.forward(tamaCuadro/2)
tortuga.write('{0:.1f}%'.format(aprobados))
tortuga.backward(tamaCuadro/2)
tortuga.setheading(270)
tortuga.forward(aprobados * 100 / total)
tortuga.setheading(0)


#mover la tortuga a otro  rectangulo
tortuga.setheading(0)
tortuga.forward(tamaCuadro*numCuadro + 20)
tortuga.pendown()
++numCuadro

#Dibujar primer cuadro aprobados
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(notables * 100 / total)
tortuga.left(90)
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(notables * 100 / total)
#Escribir texto del suspenso
tortuga.penup()
tortuga.forward(espacio)
tortuga.pendown()
tortuga.write('notables')
tortuga.penup()
tortuga.backward(espacio)
# Escribir el porcentaje sobre el cuadro
tortuga.backward((notables* 100 / total))
tortuga.setheading(0)
tortuga.forward(tamaCuadro/2)
tortuga.write('{0:.1f}%'.format(notables))
tortuga.backward(tamaCuadro/2)
tortuga.setheading(270)
tortuga.forward(notables * 100 / total)
tortuga.setheading(0)

#mover la tortuga a otro  rectangulo
tortuga.setheading(0)
tortuga.forward(tamaCuadro*numCuadro + 20)
tortuga.pendown()
++numCuadro

#Dibujar primer cuadro aprobados
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(sobresalientes * 100 / total)
tortuga.left(90)
tortuga.forward(tamaCuadro)
tortuga.left(90)
tortuga.forward(sobresalientes * 100 / total)
#Escribir texto del suspenso
tortuga.penup()
tortuga.forward(espacio)
tortuga.pendown()
tortuga.write('sobresalientes')
tortuga.penup()
tortuga.backward(espacio)
# Escribir el porcentaje sobre el cuadro
tortuga.backward((sobresalientes* 100 / total))
tortuga.setheading(0)
tortuga.forward(tamaCuadro/2)
tortuga.write('{0:.1f}%'.format(sobresalientes))
tortuga.backward(tamaCuadro/2)
tortuga.setheading(270)
tortuga.forward(sobresalientes * 100 / total)
tortuga.setheading(0)
#Salir cuando se pulse el botón en la ventana
pantalla.exitonclick()