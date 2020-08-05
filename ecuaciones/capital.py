#Un capital de C euros a un interés del x por cien anual durante n años se convierte
#en C · (1 + x/100)^n euros. Diseña un programa Python que solicite la cantidad C, el interés x y
#el número de años n y calcule el capital final solo si x es una cantidad positiva


C = int(input('Ingresa el numero de euros: '))
x = int(input('Ingresa el interes anual: '))
n = int(input('Ingresa el numero de años: '))

if x >= 0:
    C = C * ((1 + x/100)**n)
    print('\nCapital final: {0:.2f}'.format(C))
else:
    print('\nLo sentimos, no podemos calcular el capital final')