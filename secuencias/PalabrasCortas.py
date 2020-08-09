#Escribe un programa que lea una cadena y un número entero  y muestre el mensaje
#«Todas son cortas » si todas las palabras de la cadena son de longitud estrictamente menor
#que k, y «hay alguna palabra larga » en caso contrario.

cadena = input('Ingresa una cadena: ')
longitud = int(input('Ingresa la longitud de la palabra: '))

while cadena != '':
    contadorLetras = 0
    todasSonCortas = True
    anterior = ' '
    indice = 0
    while todasSonCortas == True and indice < len(cadena):
        if cadena[indice] == ' ' and anterior != ' ':
            if contadorLetras > longitud:
                todasSonCortas = False
            contadorLetras = 0
        else:
            contadorLetras += 1
        anterior = cadena[indice]
        indice += 1

    if todasSonCortas:
        print('Todas son cortas, menores o iguales que longitud ', longitud)
    else:
        print('hay alguna palabra larga')

    cadena = input("Dame una cadena: ")
    longitud = int(input('Dame un numero: '))