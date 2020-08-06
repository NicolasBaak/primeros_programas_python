numero = 7

creo_que_es_primo = True
for division in range(2, numero):
    if numero % division != 0:
        creo_que_es_primo = False
if creo_que_es_primo:
    print('El número {0} es primo.'.format(numero))
else:
    print('El numero {0} no es primo.'.format(numero))