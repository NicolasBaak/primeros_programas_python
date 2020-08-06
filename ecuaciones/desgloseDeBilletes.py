#Realiza un programa que proporcione el desglose en billetes y monedas de una
#cantidad entera de euros. Recuerda que hay billetes de 500, 200, 100, 50, 20, 10 y 5 pesos y
#monedas de 2 y 1 pesos. Debes «recorrer» los valores de billete y moneda disponibles con uno o
#más bucles for in

dinero = int(input('Dime cuanto dinero tienes: '))
for pesos in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
    billete = dinero//pesos
    if billete != 0:
        if pesos > 10:
            print('Tienes {0} billetes de {1}'.format(billete, pesos))
        else:
            print('Tienes {0} monedas de {1}'.format(billete, pesos))
    dinero = dinero % pesos