#Se ingresan dos números y se elige el mayor

a = int(input('Dame el primer número: '))
b = int(input('Dame el segundo número: '))

if a > b:
    maximo = a
else:
    maximo = b

print('El maximo es:', maximo)