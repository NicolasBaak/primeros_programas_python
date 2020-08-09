#Diseña un programa que lea una cadena y un número entero k y nos diga si todas
#sus palabras tienen una longitud de k caracteres.

cadena = input('Ingresa una cadena: ')
longitud = int(input('Ingresa la longitud de la palabra: '))

while cadena != '':
    contadorLetras = 0
    TodasLasPalabrasDeMismaLongitud = True
    anterior = ' '
    indice = 0
    while TodasLasPalabrasDeMismaLongitud == True and indice < len(cadena):
        if cadena[indice] == ' ' and anterior != ' ':
            if longitud != contadorLetras:
                TodasLasPalabrasDeMismaLongitud = False
            contadorLetras = 0
        else:
            contadorLetras += 1
        anterior = cadena[indice]
        indice += 1

    if TodasLasPalabrasDeMismaLongitud:
        print('Todas las palabras tienen una longitud ', longitud)
    else:
        print('No todas las palabras tienen la longitud {0:}'.format(longitud))

    cadena = input("Dame una cadena: ")
    longitud = int(input('Dame un numero: '))