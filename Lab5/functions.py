# Script Name: functions.py
# Author: Conor Fox 119322236


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
            fact = pos_factorial(list1[-2])
            list1.append(fact)
        print("The list is", list1)
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
            fact = neg_factorial(list1[-2])
            print(fact)
            list1.append(fact)
        print(list1)


def pos_factorial(inp):
    """
    Takes a positive number as input and returns the factorial.
    inp -- Positive integer
    return -- The factorial of the inputted number
    """
    i = 1
    accum = 1
    while i <= inp:
        accum *= i
        i += 1
    return accum


def neg_factorial(inp):
    """
    Takes a negative number as input and returns the factorial.
    inp -- Negative integer
    return -- The factorial of the inputted number5
    """
    i = -1
    accum = 1
    while i >= inp:
        accum *= i
        i -= 1
    return accum
