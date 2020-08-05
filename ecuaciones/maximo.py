#Se ingresan tres números y se elige el mayor

a = int(input('Dame el primer número: '))
b = int(input('Dame el segundo número: '))
c = int(input('Dame el tercer número: '))

candidato = a

if b > candidato:
    candidato = b
if c > candidato:
    candidato = c
maximo = candidato

print('El maximo es:', maximo)