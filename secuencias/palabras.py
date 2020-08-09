#un contador de palabras

cadena = input('Escribe una frase: ')
while cadena !='':
    cambios = 0
    anterior = ' '
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            cambios+=1
        anterior = caracter

    if cadena[-1]==' ':
        cambios-=1

    palabras = cambios + 1 #Hay una palabra más que cambios de no blanco a blanco
    print('Palabras:',palabras)

    cadena = input('Escribe una frase: ')