from turtle import Screen, Turtle
# El método speed permite controlar la velocidad con la que se desplaza la tortuga: su argumento es un número entre 0 y 10,
# donde 1 es la mínima velocidad y 10 es la máxima.

# Calificaciones ingresadas predefinidas
#suspensos = 10
#aprobados = 20
#notables = 40
#sobresalientes = 30

# Modifica el programa para que sea el usuario quien proporcione, mediante el teclado,
# el valor del porcentaje de suspensos, aprobados, notables y sobresalientes.
#suspensos = int(input("Ingresa el porcentaje de suspensos: "))
#aprobados = int(input("Ingresa el porcentaje de aprobados: "))
#notables = int(input("Ingresa el porcentaje de notables: "))
#sobresalientes = int(input("Ingresa el porcentaje de sobresalientes: "))

# Modifica el programa para que sea el usuario quien proporcione, mediante el teclado,
# el número de suspensos, aprobados, notables y sobresalientes. (Antes de dibujar el gráfico de
# pastel debes convertir esas cantidades en porcentajes).
suspensos = int(input("Ingresa el numero de suspensos: "))
aprobados = int(input("Ingresa el numero de aprobados: "))
notables = int(input("Ingresa el numero de notables: "))
sobresalientes = int(input("Ingresa el numero de sobresalientes: "))

total = suspensos + aprobados + notables + sobresalientes

suspensos = (suspensos * 100) / total
aprobados = (aprobados * 100) / total
notables = (notables * 100) / total
sobresalientes = (sobresalientes * 100) / total

#Radio del círculo
radio = 300

#Inicialización
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

#Esconder la tortuga
tortuga.hideturtle()

#Dibujo del círculo exterior.
tortuga.penup()
tortuga.goto(0, -radio)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.home()
tortuga.pendown()

#Dibujo de la línea para los suspensos.
angulo = 360 * suspensos / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir el texto para los suspensos
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('suspensos')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la línea para los aprobados.
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir el texto para los aprobados
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('aprobados')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la línea para los notables.
angulo = 360 * notables / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir el texto para los notables
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('notables')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la línea para los sobresalientes.
angulo = 360 * sobresalientes / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir el texto para los sobresalientes
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('sobresalientes')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Salir cuando se pulse el botón en la ventana
pantalla.exitonclick()