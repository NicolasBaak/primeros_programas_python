# Cálculo recursivo del número de bits necesarios para representar un
# número
def bits(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = 1 + bits(n // 2)
    return  resultado