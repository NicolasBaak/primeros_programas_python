'''Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo
saber con un mensaje adecuado.'''

a = int(input('Ingresa la edad de la primera persona: '))
b = int(input('Ingresa la edad de la segunda persona: '))

if b > a:
    print('\nLa primera persona es más joven que la segunda')
if a > b:
    print('\nLa segunda persona es más joven que la primera')
if a==b:
    print('\nAmbas personas tienen la misma edad')