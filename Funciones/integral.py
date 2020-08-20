def integral_x2(a, b, n):
    if n == 0:
        sumatoria = 0.0
    else:
        deltax = (b-a)/n
        sumatoria = 0.0
        for i in range(n):
            sumatoria += deltax * (a + i * deltax)**2
    return  sumatoria

inicio = float(input('Inicio del intervalo: '))
fin = float(input('Final del intervalo: '))
partes = int(input('Número de rectángulos: '))

print('La integral de x**2 entre {0} y {1}'.format(inicio, fin, end=''))
print('Vale aproximadamente {0:.2f}'.format(integral_x2(inicio, fin, partes)))