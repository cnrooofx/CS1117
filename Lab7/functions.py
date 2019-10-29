# Script Name: functions.py
# Author: Conor Fox 119322236


def is_stairs(list1):
    for ind in range(len(list1)):
        if ind+1 < len(list1):
            if list1[ind] < list1[ind+1]:
                print(ind)
    return
