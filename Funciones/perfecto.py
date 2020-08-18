def es_perfecto(n):
    sumatoria = 0
    for i in range(1, n):
        if n % i == 0:
            sumatoria += i
    return  sumatoria == n

def tabla_perfector(m): #muestro todos los números perfectos entre 1 y m.
    for i in range(1, m+1):
        if es_perfecto(i):
            print(i, "es un numero perfecto")


resultado = tabla_perfector(100)
print(resultado)

