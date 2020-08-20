from math import sqrt

G = 6.67e-11
MTierra = 5.97e24
RTierra = 6.37e6
MLuna = 7.35e22
RLuna = 1.74e5


def fuerzaGravitatoria(M, m, r):
    return G * M * m / r**2


def distancia(M, m, F):
    return sqrt(G * M * m / F)


def velocidadEscape(M, R):
    return sqrt(2 * G * M / R)


veTierra = velocidadEscape(MTierra, RTierra)
veLuna = velocidadEscape(MLuna, RLuna)