#Haz un programa que muestre la raíz -ésima de un número leído por teclado, para n tomando valores entre 2 y 100

numero = float(input('Dame un numero: '))

for n in range(2, 101):
    print('La raiz {0}-ésima de {1} es {2}'.format(n, numero, numero **(1/n)))