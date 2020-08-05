#Diseña un programa que, dados dos números enteros, muestre por pantalla uno de estos mensajes:
# «El segundo es el cuadrado del primero», «El segundo es menor que el cuadrado del primero »
# o bien «El segundo es mayor que el cuadrado del primero », dependiendo de la verificación de la condición
# correspondiente al significado de cada mensaje.

primero = int(input('Ingresa el primero numero: '))
segundo = int(input('Ingresa el segundo numero: '))

if segundo == (primero ** 2):
    print('El segundo es el cuadrado del primero')

if segundo <= (primero ** 2):
    print('El segundo es menor que el cuadrado del primero')

if segundo >= (primero ** 2):
    print('El segundo es mayor que el cuadrado del primero')