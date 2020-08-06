numero = 7

restos_no_nulos = 0
for division in range(2, numero):
    if numero % division != 0:
        restos_no_nulos+=1
if restos_no_nulos == numero -2:
    print('El número {0} es primo.'.format(numero))
else:
    print('El numero {0} no es primo.'.format(numero))