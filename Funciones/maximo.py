def maximo(lista):
    if len(lista) > 0:
        maximo = lista[0]
        for i in lista:
            if i > maximo:
                maximo = i
    else:
        maximo = None
    return  maximo