#Diseña un programa que, dado un número entero, determine si este es el doble de un
#número impar. (Ejemplo: 14 es el doble de 7, que es impar).

numero = int(input('Ingresa un número: '))

if ( numero/2 % 2) !=0:
    print('Es el doble de un número impar')
else:
    print('No es el doble de un número impar')