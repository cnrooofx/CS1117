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
        # Checks if value is in the list
        if value == list1[i]:
            # If it is, adds 1 to accumulator and continues
            accum += 1
            i += 1
            continue
        # If it isn't, the next value in the list is checked
        i += 1
    return accum


def index(list1, value):
    """
    Returns the first index that value occurs at in the list.
    list1 -- The list
    value -- Value to check in list
    return -- First index that value occurs at
    """
    i = 0
    while i < len(list1):
        # Checks if value is in the list
        if list1[i] == value:
            # If it is, that index is saved
            index = i
            # Only first occurance needed so break out of loop
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
    # i goes through every index in the list
    while i < len(list1):
        # If i is the specified index, the value at that index is saved
        if i == index:
            value = list1[i]
            break
        i += 1
    else:
        value = str(index)+" is not an index in the list."
    return value


def insert(list1, index, value):
    """
    Adds a value to a list at a specified index value.
    list1 -- List
    index -- Index to insert value into
    value -- Value to insert into the list1
    return -- The list with value at the specified index
    """
    # Checks the type of the list
    if isinstance(list1, str):
        i = 0
        # i goes through every index in the list
        while i < len(list1):
            # If i is the specified index:
            if i == index:
                # Gets the part of the string up to the specified index
                start = list1[:index]
                # Gets the part of the string after the specified index
                end = list1[index+1:]
                # Adds the value between the start and end
                list1 = start + value + end
                break
            i += 1
        else:
            # If index isn't in the list, value is added onto the end
            list1 = list1 + value
    # Checks the type of the list
    elif isinstance(list1, list):
        i = 0
        # i goes through every index in the list
        while i < len(list1):
            # If i is the specified index:
            if i == index:
                # The value at that index is changed to the specified value
                list1[i] = value
                break
            i += 1
        else:
            # Otherwise the value is added to the end of the list
            list1.append(value)
    return list1


def value_in_list(list1, value):
    """
    Checks to see if value is in list1.
    list1 -- List
    value -- The value to check against list1
    return -- True if value in list1, False if not
    """
    i = 0
    # i goes through every value in the list
    while i < len(list1):
        # Checks if value is in the list
        if value == list1[i]:
            # If it is, the output is True
            out = True
            break
        i += 1
    else:
        # Otherwise the output is False
        out = False
    return out


def concat(list1, list2):  # F
    """
    Returns a new list, which is a combination of list1 and list2.
    list1 -- First list
    list2 -- Second list
    return -- Combined list
    """
    return list1 + list2

    # I'm not sure how to use a while loop properly for this one
    # i = 0
    # while i < 1:
    #     new_list = list1 + list2
    #     i += 1
    # return new_list



def remove(value, list1):
    """
    Returns the list with the first occurrence of value removed from list.
    value -- Value to remove
    list1 -- The list
    return -- The list with first occurrence of value removed
    """
    i = 0
    # i goes through every value in the list
    while i < len(list1):
        # Checks if value is in the list
        if list1[i] == value:
            # Gets the part of the list up to the specified index
            start = list1[:i]
            # Gets the part of the list after the specified index
            end = list1[i+1:]
            # Puts the list back together without the value
            list1 = start + end
            break
        i += 1
    return list1
