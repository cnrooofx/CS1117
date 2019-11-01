# Script Name: functions.py
# Author: Conor Fox 119322236

import random


def is_stairs(s):
    """
    Tests if the inputted list s is a stairs (each number is one greater than
    the previous number or each number is one smaller than the previous number)
    s -- List
    return -- True if stairs, otherwise False
    """
    # Default output is False
    out = False
    # List must have more than 1 item to be a stairs
    if len(s) > 1:
        # Difference between items is the step, all items are checked against this
        # Increasing list will have step of 1, decreasing list will be -1
        stairs = ord(str(s[1]).lower()) - ord(str(s[0]).lower())
        for i in range(len(s)-1):
            # If the value +-1 is not equal to the next value in the list then it is not a stairs
            if ord(str(s[i]).lower())+stairs != ord(str(s[i+1]).lower()):
                out = False
                break
            else:
                out = True
    return out


def factorial(n):
    """
    Takes a positive number as input and returns the factorial.
    inp -- Positive integer
    return -- The factorial of the inputted number
    """
    accum = n
    if n >= 0:
        i = 1
        accum = 1
        while i <= n:
            accum *= i
            i += 1
    else:
        accum = -1
    return accum


def gremlins(name):
    dinnertime = True
    bright = False
    triplet = False
    fate = ""
    # Goes through the functions 5 times.
    for i in range(5):
        # Random number to choose the function
        call = random.randint(1, 3)
        if call == 1:
            dinnertime = okay_to_feed(random.randint(0, 24))
            if dinnertime is False:
                name = "Stripe"
        elif call == 2:
            bright = is_too_bright(random.randint(25, 100))
            if bright is True:
                break
        else:
            wet = is_wet()
            if wet is True:
                triplet = True
    if bright is False and triplet is False:
        fate = "rules!"
    elif triplet is True:
        fate = "is a triplet"
    elif bright is True:
        fate = "is no more"
    print(name, fate)


def is_wet():
    boolean = random.randint(1, 2)
    if boolean == 1:
        out = False
    else:
        out = True
    return out


def is_too_bright(lux_level):
    if lux_level > 80:
        out = True
    else:
        out = False
    return out


def okay_to_feed(time):
    if time > 0 and time < 4:
        out = False
    else:
        out = True
    return out
