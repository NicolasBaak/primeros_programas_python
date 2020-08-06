#Haz un programa que muestre la tabla de multiplicar de un número introducido por
#teclado por el usuario

numero = int(input('Dame un número: '))

for multiplicacion in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print('{0} x {1} = {2}'.format(numero, multiplicacion, numero*multiplicacion))