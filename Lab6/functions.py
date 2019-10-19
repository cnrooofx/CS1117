# Script Name: functions.py
# Author: Conor Fox 119322236


def count(list1, value):
    i = 0
    accum = 0
    while i < len(list1):
        if value == list1[i]:
            accum += 1
            i += 1
            continue
        i += 1
    print(accum)


def index(list1, value):
    if value in list1:
        print(list1.index(value))
    else:
        print(-1)


def get_value(list1, index):
    if index in range(len(list1)):
        print(list1[index])
    else:
        print(index, "is not an index in", list1)


def insert(list1, index, value):
    if type(list1) is str:
        if index in range(len(list1)):
            start = list1[:index]
            end = list1[index+1:]
            print(start + value + end)
        else:
            print(list1 + value)
    elif type(list1) is list:
        value = [value]
        if index in range(len(list1)):
            start = list1[:index]
            end = list1[index+1:]
            print(start + value + end)
        else:
            print(list1 + value)
    else:
        print("list1 is neither 'str' nor 'list' and is therefore not indexable and reassignable")


def value_in_list(list1, value):
    if value in list1:
        out = True
    else:
        out = False
    return out


def concat(list1, list2):
    print(list1 + list2)
