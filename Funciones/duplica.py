# Diseña una función duplica que reciba una lista de números y la modifique duplicando
# el valor de cada uno de sus elementos. (Ejemplo: la lista [1, 2, 3] se convertirá en la lista
# [2, 4, 6] ).

def duplica(lista):
    resultado = []
    for elemento in lista:
        resultado.append(elemento * 2)
    return resultado


lista = [1, 2, 3]
print(duplica(lista))