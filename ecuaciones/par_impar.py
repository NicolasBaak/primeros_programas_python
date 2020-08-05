'''Diseña un programa que, dado un número entero, muestre por pantalla el mensaje «El número es par»  cuando el número sea par
y el mensaje «El numero es impar» cuando sea impar.'''

a = int(input('Ingresa un numero: '))

if (a % 2) == 0:
    print('\nEl numero es par')

if (a % 2) != 0:
    print('\nEl numero es impar')