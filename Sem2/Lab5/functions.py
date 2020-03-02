# Script Name: functions.py
# Author: Conor Fox 119322236


# 1
def factorialL(n):
    if n == 1:
        return 1
    else:
        return n * factorialL(n-1)


# 2
def hailStoneR(n):
    start = [n]
    if n == 1:
        return [1]
    elif n % 2 == 0:
        n //= 2
    else:
        n = (3 * n + 1)
    return start + hailStoneR(n)
