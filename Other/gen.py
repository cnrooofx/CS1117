
import random
import string


def rand_int_list(length=10, start=0, end=100):
    rand_list = []
    i = 0
    while i < length:
        rand_list.append(random.randint(start, end))
        i += 1
    return rand_list


def rand_ascii_list(length=10, upper=True, lower=True):
    i = 0
    rand_list = []
    if upper is False and lower is False:
        upper = True
        lower = True
    if upper is True and lower is True:
        while i < length:
            rand_list.append(random.choice(string.ascii_letters))
            i += 1
    elif upper is True and lower is False:
        while i < length:
            rand_list.append(random.choice(string.ascii_uppercase))
            i += 1
    else:
        while i < length:
            rand_list.append(random.choice(string.ascii_lowercase))
            i += 1
    return rand_list


print(rand_ascii_list(length=30, upper=False, lower=True))
