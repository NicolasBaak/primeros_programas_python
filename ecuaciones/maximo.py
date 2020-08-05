#Se ingresan tres números y se elige el mayor

a = int(input('Dame el primer número: '))
b = int(input('Dame el segundo número: '))
c = int(input('Dame el tercer número: '))

if a > b:
    if a > c:
        maximo = a
    else:
        maximo = c
else:
    if b > c:
        maximo = b
    else:
        maximo = c

print('El maximo es:', maximo)