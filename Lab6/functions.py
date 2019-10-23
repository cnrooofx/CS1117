# Script Name: functions.py
# Author: Conor Fox 119322236


def count(list1, value):
    """
    Return the number of times value occurs in the list.
    list1 -- The list
    value -- Value to look for in the list
    return -- Number of times that value is in the list
    """
    i = 0
    accum = 0
    while i < len(list1):
        if value == list1[i]:
            accum += 1
            i += 1
        i += 1
    return accum


def index(list1, value):
    """
    Returns
    """
    i = 0
    while i < len(list1):
        if list1[i] == value:
            index = i
            break
        i += 1
    else:
        index = -1
    return index


def get_value(list1, index):
    """
    Returns the value at the specified index
    list1 -- The list
    index -- Index value to check
    return -- The value at index
    """
    i = 0
    while i < len(list1):
        if i == index:
            value = list1[i]
            break
        i += 1
    else:
        value = "index is not an index in list1"
    return value


def insert(list1, index, value):
    """
    Adds a value to a list at a specified index value.
    list1 -- List
    index -- Index to insert value into
    value -- Value to insert into the list1
    return -- The list with value at the specified index
    """
    if type(list1) is str:
        i = 0
        while i < len(list1):
            if i == index:
                start = list1[:index]
                end = list1[index+1:]
                list1 = start + value + end
                break
            i += 1
        else:
            list1 = list1 + value
    elif type(list1) is list:
        i = 0
        while i < len(list1):
            if i == index:
                list1[i] = value
                break
            i += 1
        else:
            list1.append(value)
    return list1


def value_in_list(list1, value):
    """
    Checks to see if value is in list1
    list1 -- List
    value -- The value to check against list1
    return -- True if value in list1, False if not
    """
    i = 0
    while i < len(list1):
        if value == list1[i]:
            out = True
            break
        i += 1
    else:
        out = False
    return out


def concat(list1, list2):  # F
    """
    Returns a new list, which is a combination of list1 and list2
    """
    new_list = list1 + list2
    return new_list


def remove(value, list1):
    """
    Returns the list with the first occurrence of value removed from list.
    value -- Value to remove
    list1 -- The list
    return -- The list with first occurrence of value removed
    """
    if type(list1) is list:
        i = 0
        while i < len(list1):
            if list1[i] == value:
                list.remove(value)
                break
            i += 1
    elif type(list1) is str:
        i = 0
        while i < len(list1):
            if list1[i] == value:
                start = list1[:i]
                end = list1[i+1:]
                list1 = start + end
                break
            i += 1
    return list1
