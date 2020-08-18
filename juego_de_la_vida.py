import pygame
import numpy as np

pygame.init()
#Ancho y alto de la pantalla
width, height = 1000,1000
#Creacion de la pantalla
screen = pygame.display.set_mode((height, width))

#Color del fondo
bg = 25, 25, 25
#pintams el fondo con el color elegido
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC
dimCH = height / nyC

#Bulce de ejecucion
while True:
    pass
