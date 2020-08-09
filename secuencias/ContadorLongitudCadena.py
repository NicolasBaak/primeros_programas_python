#Diseña un programa que lea una cadena y un número entero k y nos diga cuántas
#palabras tienen una longitud de k caracteres

cadena = input('Dame una cadena: ')
longitud = int(input('Dame una longitud de palabra: '))

while cadena != '':
    #Numero de letras antes de un cambio de palabra
    contadorLetras = 0
    #Numero de palabras con la longitud ingresada
    contadorPalabras = 0
    anterior = ' '
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            if longitud == contadorLetras:
                contadorPalabras+=1
            contadorLetras = 0
        elif caracter != ' ':
            contadorLetras+=1
        anterior = caracter

    if cadena[-1] != ' ' and longitud == contadorLetras:
        contadorPalabras += 1
    print('Palabras con una longitud de {0:} letras: {1:}'.format(longitud, contadorPalabras))

    cadena = input("Dame una cadena: ")
    longitud = int(input('Dame un numero: '))