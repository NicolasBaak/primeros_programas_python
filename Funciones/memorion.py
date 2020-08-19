from random import randrange
from turtle import Screen, Turtle
from time import sleep

CeldaCerrada = 0
CeldaAbierta = 1
CeldaTemporalmenteAbierta = 2


def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([None] * columnas)
    return matriz


def inicializa_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = CeldaCerrada


def rellena_simbolos(simbolo):
    numsimbolo = 0
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            simbolo[i][j] = chr(ord('a') + numsimbolo // 2)
            numsimbolo += 1

    for i in range(1000):
        [f1, c1] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
        [f2, c2] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
        tmp = simbolo[f1][c1]
        simbolo[f1][c1] = simbolo[f2][c2]
        simbolo[f2][c2] = tmp


def dibuja_celda(baldosa, simbolo, i, j):
    global tortuga
    tortuga.penup()
    tortuga.goto(j + .5, i)
    tortuga.begin_fill()
    if baldosa[i][j] == CeldaCerrada:
        tortuga.fillcolor('blue')
        tortuga.circle(.5)
        tortuga.goto(j + .5, i + .25)
        tortuga.write(simbolo[i][j])
    elif baldosa[i][j] == CeldaAbierta:
        tortuga.fillcolor('white')
        tortuga.circle(.5)
        tortuga.goto(j + .5, i + .25)
        tortuga.write(simbolo[i][j])
    else:
        tortuga.fillcolor('yellow')
        tortuga.circle(.5)
        tortuga.goto(j + .5, i + .25)
        tortuga.write(simbolo[i][j])
    tortuga.end_fill()
    tortuga.pendown()


def dibuja_tablero(tablero, simbolo):
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            dibuja_celda(tablero, simbolo, i, j)


def clic(x, y):
    global pantalla, tablero, simbolo, temporal1, temporal2
    pantalla.onclick(None)
    [j, i] = [int(x), int(y)]
    if 0 <= i < len(tablero) and 0 <= j <= len(tablero[0]):
        if tablero[i][j] == CeldaCerrada:
            if temporal1 == None:
                temporal1 = [i, j]
                tablero[i][j] = CeldaTemporalmenteAbierta
            else:
                temporal2 = [i, j]
                tablero[i][j] = CeldaTemporalmenteAbierta
            dibuja_celda(tablero, simbolo, i, j)
            if temporal2 != None:
                if simbolo[temporal1[0]][temporal1[1]] == simbolo[temporal2[0]][temporal2[1]]:
                    tablero[temporal1[0]][temporal1[1]] = CeldaAbierta
                    tablero[temporal2[0]][temporal2[1]] = CeldaAbierta
                else:
                    sleep(0.5)
                    tablero[temporal1[0]][temporal1[1]] = CeldaCerrada
                    tablero[temporal2[0]][temporal2[1]] = CeldaCerrada
                dibuja_celda(tablero, simbolo, temporal1[0], temporal1[1])
                dibuja_celda(tablero, simbolo, temporal2[0], temporal2[1])
                temporal1 = None
                temporal2 = None
        dibuja_celda(tablero, simbolo, i, j)

    if todas_abiertas(tablero):
        pantalla.bye()
    else:
        pantalla.onclick(clic)


def todas_abiertas(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == CeldaCerrada:
                return False
    return True

def menu():
    opc = 0
    while opc > 3 or opc <= 0:
        print('Selecciona tu nivel de dificultad: ')
        print('1) Facil')
        print('2) Normal')
        print('3) Dificil')
        opc = int(input('¿Dificultad 1, 2, ó 3?: '))

    if opc == 1:
        return [3, 4]
    elif opc == 2:
        return [4, 6]
    else:
        return [6, 8]


# Programa principal
[filas, columnas] = menu()

pantalla = Screen()
pantalla.setup(columnas * 50, filas * 50)
pantalla.screensize(columnas * 50, filas * 50)
pantalla.setworldcoordinates(-.5, -.5, columnas + .5, filas + .5)
pantalla.delay(0)

tortuga = Turtle()
tortuga.hideturtle()
simbolo = crea_matriz(filas, columnas)
tablero = crea_matriz(filas, columnas)

temporal1 = None
temporal2 = None
inicializa_tablero(tablero)
rellena_simbolos(simbolo)
dibuja_tablero(tablero, simbolo)

pantalla.onclick(clic)

pantalla.mainloop()
