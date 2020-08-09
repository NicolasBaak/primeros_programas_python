#Diseña un programa que lea una cadena y un número entero k y nos diga si alguna
#de sus palabras tiene una longitud de k caracteres.

cadena = input('Ingresa una cadena: ')
longitud = int(input('Ingresa la longitud de la palabra: '))

while cadena != '':
    contadorLetras = 0
    ExiteUnaPalabraDeDichaLongitud = False
    anterior = ' '
    indice = 0
    while ExiteUnaPalabraDeDichaLongitud == False and indice < len(cadena):
        if cadena[indice] == ' ' and anterior != ' ':
            if longitud == contadorLetras:
                ExiteUnaPalabraDeDichaLongitud = True
            contadorLetras = 0
        else:
            contadorLetras+=1
        anterior = cadena[indice]
        indice+=1

    if ExiteUnaPalabraDeDichaLongitud:
        print('Si hay al menos una palbra de longitud {0:} y es: {1:}'.format(longitud, cadena[indice-1-longitud: indice-1]))
    else:
        print('No  hay ninguna palara de longitud ',longitud)

    cadena = input("Dame una cadena: ")
    longitud = int(input('Dame un numero: '))