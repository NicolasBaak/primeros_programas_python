
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n


def fibonacci_iterativo(n):
    if n == 1 or n == 2:
        f = 1
    else:
        f1 = f2 = 1
        for i in range(3, n+1):
            [i, f1, f2] = [f1+f2, f2, f]
        return  f
print('Fibonacci de 12:',fibonacci(12))