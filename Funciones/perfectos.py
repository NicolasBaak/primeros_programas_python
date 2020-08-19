# Diseña un procedimiento que, dada una lista de números, la modifique para que solo
# sobrevivan a la llamada aquellos números que son perfectos.


def es_perfecto(n):
    sumatoria = 0
    for i in range(1, n):
        if n % i == 0:
            sumatoria += i
    return sumatoria == n


def sobreviven_num_perfectos(lista):
    resultado = []
    for elemento in lista:
        if es_perfecto(elemento):
            resultado.append(elemento)
    return resultado


lista = [1, 6, 28, 34, 25]
print('Numeros perfectos: ', sobreviven_num_perfectos(lista))

