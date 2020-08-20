# El método de la bisección permite encontrar un cero de una función matemática f(x) en un
# intervalo [a,b] si f(x) es continua en dicho intervalo y f(a) y f(b) son de distinto signo.


def f(x):
    return  x**2-2*x-2


def biseccion(a, b, epsilon=1e-5):
    if f(a) == 0 and f(b) == 0:
        return 0
    else:
        c = (a+b)/2
        fc = f(c)
        while fc != 0 and b - a > epsilon:
            if f(a) * fc > 0:
                a = c
            elif f(b) * fc > 0:
                b = c
            c = (a+b)/2
        return c


print('El cero está en:', biseccion(0.5, 3.5, 1e-5))