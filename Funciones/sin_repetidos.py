# una función que recibe una lista y devuelve
# otra cuyos elementos son los de la primera, pero sin repetir ninguno
def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


# Diseña una función que reciba dos listas y devuelva los elementos comunes a ambas,
# sin repetir ninguno (intersección de conjuntos).
def comunes_sin_repetidos(lista1, lista2):
    resultado = []
    for elemento in lista1:
        if elemento not in resultado and elemento in lista2:
            resultado.append(elemento)
    for elemento in lista2:
        if elemento not in resultado and elemento in lista2:
            resultado.append(elemento)
    return resultado


# Diseña una función que reciba dos listas y devuelva los elementos que pertenecen a
# una o a otra, pero sin repetir ninguno (unión de conjuntos).
def union_sin_repetidos(lista1, lista2):
    resultado = []
    for elemento in lista1:
        if elemento not in resultado and (elemento in lista2 or elemento in lista1):
            resultado.append(elemento)
    for elemento in lista2:
        if elemento not in resultado and (elemento in lista2 or elemento in lista1):
            resultado.append(elemento)
    return resultado


# Diseña una función que reciba dos listas y devuelva los elementos que pertenecen a
# la primera pero no a la segunda, sin repetir ninguno (diferencia de conjuntos).
def diferencia_sin_repetidos(lista1, lista2):
    resultado = []
    for elemento in lista1:
        if elemento not in resultado and elemento not in lista2:
            resultado.append(elemento)
    return resultado


# Diseña una función que, dada una lista de números, devuelva otra lista que solo
# incluya sus números impares.
def solo_impares(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado and ( elemento % 2 != 0) and elemento != 1:
            resultado.append(elemento)
    return resultado


# Diseña una función que, dada una lista de números, devuelva otra lista que solo
# incluya sus números impares.
def nombres_iguales(lista, letra):
    resultado = []
    for nombre in lista:
        if nombre not in resultado and nombre[0] == letra:
            resultado.append(nombre)
    return resultado

#programa principal
una_lista = sin_repetidos([1, 2, 1, 1, 2, 3, 4, 3, 4, 4])
print(una_lista)

dos_listas_sin_repetidos = comunes_sin_repetidos([1, 2, 3, 3, 1], [2, 2, 3])
print(dos_listas_sin_repetidos)

dos_listas_sin_repetidos = union_sin_repetidos([1, 2, 3, 3, 1, 4, 5], [2, 2, 6, 3])
print(dos_listas_sin_repetidos)

dos_listas_sin_repetidos = diferencia_sin_repetidos([1, 2, 3, 3, 1, 4, 5], [2, 2, 6, 3])
print(dos_listas_sin_repetidos)

una_lista = solo_impares([1, 2, 9, 7, 2, 3, 4, 3, 4, 4])
print(una_lista)

una_lista = nombres_iguales(['Juan', 'Nico', 'Axel', 'Maria', 'Mario', 'Monserrat'], "M")
print(una_lista)

