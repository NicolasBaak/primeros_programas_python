#Escribe un programa que lea una cadena y un número entero  y muestre el mensaje
#«Hay palabras largas » si alguna de las palabras de la cadena es de longitud mayor o igual
#que k, y «No hay palabras largas» en caso contrario

cadena = input('Ingresa una cadena: ')
longitud = int(input('Ingresa la longitud de la palabra: '))

while cadena != '':
    contadorLetras = 0
    hayPalabrasLargas = False
    anterior = ' '
    indice = 0
    while hayPalabrasLargas == False and indice < len(cadena):
        if cadena[indice] == ' ' and anterior != ' ':
            if contadorLetras > longitud:
                hayPalabrasLargas = True
            contadorLetras = 0
        else:
            contadorLetras += 1
        anterior = cadena[indice]
        indice += 1

    if hayPalabrasLargas:
        print('Hay palabras largas de longitud: ', longitud)
    else:
        print('No hay palabras largas')

    cadena = input("Dame una cadena: ")
    longitud = int(input('Dame un numero: '))