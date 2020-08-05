"""Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
«Es paréntesis» solo si el carácter leído es un paréntesis abierto o cerrado."""

letra = input('Presiona un caracter: ')

if letra == '(' or letra == ')':
    print('Es paréntesis')
