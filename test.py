from math import pi

'''
--------Perimetro de un circulo
'''
radio = 1
perimetro = 2 * pi * radio
print("Perimetro de un circulo: "+str(perimetro)+"cm\n")

'''
--------Perimetro y area de un cuadrado
'''
lado = 3
perimetro = lado * 4
area = lado * lado
print("Perimetro cuadrado: "+str(perimetro)+ "cm\nArea cuadrado: "+str(area)+"cm2")

'''
--------Area del triangulo
'''
base = 3
altura = 5
area = .5 * base * altura
print("\nArea del triangulo",area,"cm2")

'''
-------Perimetro de un rectangulo
'''
lado = 4
lado2 = 6
perimetro = lado * 2 + lado2 * 2
area = lado * lado2
print("\nPerimetro rectangulo: "+str(perimetro)+ "cm\nArea rectangulo: "+str(area)+"cm2")
