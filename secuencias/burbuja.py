lista = [2, 26, 4, 5, 1]

for i in range(1, len(lista)):
    for j in range(0,len(lista)-1):
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
print(lista)
