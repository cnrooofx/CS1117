# Recursion


def fibonacciI(n):
    if n < 2:
        return n
    f1 = 0
    f2 = 1
    for count in range(2, n+1):
        fib = f1 + f2
        f1 = f2
        f2 = fib
    return fib


print(fibonacciI(6))


def fibonacciR(n):
    if n < 2:
        return n
    return fibonacciR(n-1) + fibonacciR(n-2)


print(fibonacciR(6))
