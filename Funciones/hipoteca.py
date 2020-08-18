# Vamos a adquirir una vivienda y para eso necesitaremos una hipoteca. La cuota
# mensual m que hemos de pagar para amortizar una hipoteca de h euros a lo largo de n años a
# un interés compuesto del i por cien anual se calcula con la fórmula: m = (hr)/(1-(1+r)**-12n)

# Diseña una función que nos devuelva la cantidad de euros que habremos pagado
# finalmente al banco si abrimos una hipoteca de h euros a un interés del i por cien en n años.

# Diseña una función que nos diga qué cantidad de intereses (en euros) habremos
# pagado finalmente al banco si abrimos una hipoteca de h euros a un interés del i por cien en n
# años. Si te conviene, puedes utilizar las funciones que definiste en los ejercicios anteriores.


def cuota_mensual(h, n, i):
    r = i / (100 * 12)

    return round((h * r) / (1 - (1 + r) ** (-12 * n)), 2)


def cuota_total_pagada(h, n, i):
    return round(cuota_mensual(h, n, i) * n * 12, 2)


def cantidad_de_intereses_pagados(h, n, i):
    return cuota_total_pagada(h, n, i) - h


def porcentaje_del_capital(h, n, i):
    cantidad_pagada = cantidad_de_intereses_pagados(h, n, i)
    return (cantidad_pagada * 100)/h

def cuota_mensual_en_diferentes_años(h, n, i):
    for opc in n:
        print('Su cuota mensual es de {0} en {1} años'.format(cuota_mensual(h, opc, i), opc))

def dinero_total_de_coutas_mensuales(h, n, i):
    for opc in n:
        print(' La cantidad total de coutas mensuales pagadas es de {0} en {1} años'.format(cuota_total_pagada(h, opc, i), opc))

h = 150000
n = [10, 15, 20, 25]
i = 4.75
print(' Su cuota mensual es:',cuota_mensual(150000, 15, 4.75))
print(' La cantidad total de coutas mensuales pagadas es de: ', cuota_total_pagada(150000, 15, 4.75))
print(' La cantidad de intereses pagados es de:', cantidad_de_intereses_pagados(150000, 15, 4.75))
print(' El porcentaje de intereses pagados sobre el total de la hipoteca es el: ', porcentaje_del_capital(150000, 15, 4.75), '%')

print('\nProcedimientos para multiples años:')
cuota_mensual_en_diferentes_años(h, n, i)
dinero_total_de_coutas_mensuales(h, n, i)