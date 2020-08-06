numero = int(input('Dame un número: '))

if numero > 1:
    creo_que_es_primo = True
    divisor = 2
    while divisor < numero and creo_que_es_primo:
        if numero % divisor == 0:
            creo_que_es_primo = False
        divisor +=1
else:
    creo_que_es_primo = False

if creo_que_es_primo:
    print('El número {0} es primo.'.format(numero))
else:
    print('El numero {0} no es primo.'.format(numero))
