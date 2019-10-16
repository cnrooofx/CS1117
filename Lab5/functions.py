# Script Name: functions.py
# Author: Conor Fox 119322236

import math


def while_loop(max_number=10, even=False, factorial=False):
    list1 = []
    i = 1
    accum = 0
    if max_number > 0:
        while i <= max_number:
            if even is True and i % 2 != 0:
                i += 1
                continue
            if i > 12:
                break
            list1.append(i)
            accum += i
            i += 1
        list1.append(accum)
        if factorial is True:
            fact = math.factorial(list1[-2])
            list1.append(fact)
        print(list1)
    elif max_number <= 0:
        while i >= max_number:
            if even is True and i % 2 != 0:
                i -= 1
                continue
            if i < -12:
                break
            list1.append(i)
            accum += i
            i -= 1
        list1.append(accum)
        if factorial is True:
            fact = math.factorial(abs(list1[-2]))
            list1.append(fact)
        print(list1)
