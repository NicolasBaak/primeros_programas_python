numero = int(input('Dame un número: '))

for potencia in [2, 3, 4, 5]:
    print('{0} elevado a {1} es {2}'.format(numero, potencia, numero**potencia))