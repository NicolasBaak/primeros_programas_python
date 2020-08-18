#Pedimos la dimensión de la primera matriz y el número de columnas de la segunda.

p = int(input('Dime el número de filas de A: '))
q = int(input('DIme el número de columnas de A (y filas de B): '))
r = int(input('DIme el número de columnas de B: '))

#creamos dos matrices nulas...
A=[]
for i in range(p):
    A.append([0]*q)

B=[]
for i in range(q):
    B.append([0]*r)

# ...y leemos su contenido de teclado
print('Lectura de la matriz A')
for i in range(p):
    for j in range(q):
        A[i][j] = float(input('Componente ({0},{1}): '.format(i, j)))

print('Lectura de la matriz B')
for i in range(q):
    for j in range(r):
        B[i][j] = float(input('Componente ({0},{1}): '.format(i, j)))

#Creamos la matriz nula para el resultado...

C=[]
for i in range(p):
    C.append([0]*r)

#Y se efectua el cálculo del producto

for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] += A[i][k] * B[k][j]

#Y mostramos el resultado por pantalla
print('Multiplicación: ')
for i in range(p):
    for j in range(r):
        print(C[i][j], end='\t|\t')
    print()