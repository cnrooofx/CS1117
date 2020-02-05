
import random
import string


def rand_ascii_list(length=10, upper=True, lower=True):
    i = 0
    rand_list = []
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


def list_of_lists(lists=5, length=10, start=0, end=100):
    if lists == 1:
        return [random.randint(start, end) for i in range(length)]
    return [[random.randint(start, end) for i in range(length)]
            for j in range(lists)]


# print(list_of_lists(1, 5, 9000, 11000))

print(rand_ascii_list(length=10, upper=True, lower=True))
