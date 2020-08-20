def resuelve_hanoi(n, inicial, final):
    if n == 1:
        print('Mover disco superior de aguja', inicial, 'a', final)
    else:
        # Determinar cual es la aguja libre
        if inicial != 1 and final != 1:
            libre = 1
        elif inicial != 2 and final != 2:
            libre = 2
        else:
            libre = 3
        # Primer subproblema mover n-1 discos de inicial a libre
        resuelve_hanoi(n-1, inicial, libre)
        # Transferir el disco grande a su posicion final
        print('Mover disco superior de aguja', inicial, 'a', final)
        # Segundo subproblema: mover n-1 discos de libre a final
        resuelve_hanoi(n-1, libre, final)

resuelve_hanoi(64, 1, 3)