# Script Name: functions.py
# Author: Conor Fox 119322236


def is_stairs(list1):
    for i in enumerate(list1):
        if list1[i] < len(list1):
            print(i)
            # if list1[index] < list1[index+1]:
            # print(index)


list1 = [1, 2, 3, 4, 5]

for index, val in enumerate(list1):
    print(val, "is a value in", list1, "at index", index)
