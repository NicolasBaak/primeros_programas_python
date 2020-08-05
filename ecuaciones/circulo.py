from math import  pi

#Nuestro programa podría empezar pidiendo el radio del círculo. A continuación, podría mostrar
#un menú con tres opciones: «calcular el diámetro», «calcular el perímetro» y «calcular el área».
#Podríamos etiquetar cada opción con una letra y hacer que el usuario tecleara una de ellas. En
#función de la letra tecleada, calcularíamos una cosa u otra.

radio = float(input('Dame el radio de un círculo: '))

#Menu
print('Escoge una opción: ')
print('(a) Calcular el diámetro.')
print('(b) Calcular el perimetro.')
print('(c) Calcular el área.')
opcion = input('Teclea a, b ó c y pulsa el retorno de carro: ')

#operaciones
if opcion == 'a' or opcion == 'A': #Cálculo del diámetro.
    diametro = 2 * radio
    print('El diámetro es {0}.'.format(diametro))
elif opcion == 'b' or opcion == 'B': #Cálculo de perímetro.
    perimetro = 2 * pi * radio
    print('El perimetro es {0}.'.format(perimetro))
elif opcion == 'c' or opcion == 'C': #Cálculo del área.
    area = pi * radio **2
    print('El área es {0}.'.format(area))
else:
    print('Solo hay tres opciones: a, b ó c')
    print('Tú has tecleado "{0}".'.format(opcion))