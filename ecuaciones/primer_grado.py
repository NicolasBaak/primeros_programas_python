print('Programa para la resolución de la ecuación ax+b=0')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

try:
    x = -b/a
    print('Solución: ', x)
except:
    if b != 0:
        print('La ecuación no tiene solución real.')
    else:
        print('La ecuación tiene infinitas soluciones.')