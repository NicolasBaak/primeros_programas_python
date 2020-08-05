print('Programa para la resolución de la ecuación ax+b=0')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

if a != 0:
    x = -b/a
    print('Solución: ', x)

if a == 0:
    if b != 0:
        print('La ecuación no tiene solución real.')
    if b ==0:
        print('La ecuación tiene infinitas soluciones.')