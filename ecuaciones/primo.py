#Vamos a hacer que el programa pida un número y nos muestre por pantalla los números primos entre 1 y el que hemos introducido

limite = int(input('Dame un número: '))

for numero in range(2, limite+1):
    creo_que_es_primo=True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
    if creo_que_es_primo:
        print(numero, end=' ')
print()