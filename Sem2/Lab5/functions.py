# Script Name: functions.py
# Author: Conor Fox 119322236


def hailStoneR(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        n //= 2
    else:
        n = (3 * n + 1)
    hailStoneR(n)
