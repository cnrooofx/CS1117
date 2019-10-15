# ScriptName: functions.py
# Author: Conor Fox 119322236


def while_loop(max_number=10):
    """
    Loops from 1
    """
    if max_number >= 0:
        list1 = []
        i = 1
        while i <= max_number:
            list1.append(i)
            i += 1
        print(list1)
    else:
        print("Input is not a positive number.")


def while_loop_v2(max_number=10):
    list1 = []
    i = 1
    if max_number > 0:
        while i <= max_number:
            list1.append(i)
            i += 1
        print(list1)
    elif max_number <= 0:
        while i >= max_number:
            list1.append(i)
            i -= 1
        print(list1)


def while_loop_v3(max_number=10):
    list1 = []
    i = 1
    accum = 0
    if max_number > 0:
        while i <= max_number:
            list1.append(i)
            accum += i
            i += 1
        list1.append(accum)
        print(list1)
    elif max_number <= 0:
        while i >= max_number:
            list1.append(i)
            accum += i
            i -= 1
        list1.append(accum)
        print(list1)


def while_loop_v4(max_number=10):
    list1 = []
    i = 1
    accum = 0
    if max_number > 0:
        while i <= max_number:
            list1.append(i)
            i += 1
            accum += i
            if i > 12:
                break
        list1.append(accum)
        print(list1)
    elif max_number <= 0:
        while i >= max_number:
            list1.append(i)
            i -= 1
            accum += i
            if i < -12:
                break
        list1.append(accum)
        print(list1)
