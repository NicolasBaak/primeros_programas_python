# Pedimos la dimensión de la matriz
m = int(input('Dime el número de filas: '))
n = int(input('Dime el número de columnas: '))

# creamos dos matrices nula...
A = []
for i in range(m):
    A.append([0] * n)

B = []
for i in range(m):
    B.append([0] * n)

# ...y leemos su contenido de teclado
print('Lectura de la matriz A')
for i in range(m):
    for j in range(n):
        A[i][j] = float(input('Componente ({0},{1}): '.format(i, j)))

print('Lectura de la matriz B')
for i in range(m):
    for j in range(n):
        B[i][j] = float(input('Componente ({0},{1}): '.format(i, j)))

#Construimos otra matriz nula para albergar el resultado
C = []
for i in range(m):
    C.append([0]*n)

#Empieza el cálculo de la suma.
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

#Y mostramos el resultado por pantalla
print('Suma: ')
for i in range(m):
    for j in range(n):
        print(C[i][j], end=' | ')
    print()