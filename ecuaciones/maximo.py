#Se ingresan cinco números y se elige el mayor

a = int(input('Dame el primer número: '))
b = int(input('Dame el segundo número: '))
c = int(input('Dame el tercer número: '))
d = int(input('Dame el cuarto número: '))
e = int(input('Dame el quinto número: '))

candidato = a

if b > candidato:
    candidato = b
if c > candidato:
    candidato = c
if d > candidato:
    candidato = d
if e > candidato:
    candidato = e

maximo = candidato

print('El maximo es:', maximo)