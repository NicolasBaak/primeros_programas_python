m = int(input('Ingresa hasta que numero vamos a sumar: '))
n = int(input('Ingresa la cantidad que se ira sumando cada vez: '))
sumatorio = 0
i = 0
if n > m:
    print('n debe ser menor o igual que m')
else:
    while i < m:
        i += n
        sumatorio += i
    print(sumatorio)

    for i in range(0, m+1):
        i+=n
    print('usando for-in: ',sumatorio)
