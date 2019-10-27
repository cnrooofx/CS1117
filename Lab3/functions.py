# Script Name: functions.py
# Author: Conor Fox 119322236

import math


def three_numbers(num1, num2, num3):
    """
    If three inputted numbers are the same output is true, otherwise false
    num1 -- First imputted number
    num2 -- Second imputted number
    num3 -- Third imputted number
    """
    if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
        if num1 == num2 == num3:
            out = True
        else:
            out = False
    else:
        out = "Input is not an integer"
    return out


def seasons(number):
    """
    Takes number between 1 and 4 and displays corresponding season
    number -- Between 1 and 4
    """
    if number == 1:
        out = "Spring"
    elif number == 2:
        out = "Summer"
    elif number == 3:
        out = "Autumn"
    elif number == 4:
        out = "Winter"
    else:
        out = "Please enter an integer between 1 and 4"
    return out


def grades(score):
    """
    Gives grade based on test score
    score -- Test score between 0 and 100
    """
    if isinstance(score, int):
        if score >= 0 and score <= 24:
            out = "F"
        elif score >= 25 and score <= 39:
            out = "E"
        elif score >= 40 and score <= 54:
            out = "D"
        elif score >= 55 and score <= 69:
            out = "C"
        elif score >= 70 and score <= 84:
            out = "B"
        elif score >= 85 and score <= 100:
            out = "A"
        else:
            out = "X"
    else:
        out = "Error - please enter an integer between 0 and 100"
    return out


def equal_numbers(num1, num2):
    """
    Takes two numbers, if equal gives the square root, if different gives square of both numbers
    num1 -- First imputted number
    num2 -- Second imputted number
    """
    if isinstance(num1, int) and isinstance(num2, int):
        if num1 == num2:
            square_root = math.sqrt(num1)
            out = "The square root of %d is %.3f" % (int(num1), float(square_root))
        else:
            square_num1 = num1 ** 2
            square_num2 = num2 ** 2

            out = "\"%d\" squared is \"%d\" and \"%d\" squared is \"%d\"" % (num1, square_num1, num2, square_num2)
    else:
        out = "Error - Input is not an integer"
    return out


def fizz_buzz(number):
    """
    Like game of FizzBuzz, if number is a multiple of 3 prints Fizz, if number is a multiple of 5 prints Buzz and if number is a multiple of both prints FizzBuzz
    number -- Number to be inputted
    """
    if isinstance(number, int):
        if (number % 5) == 0 and (number % 3) == 0:
            out = "FizzBuzz"
        elif (number % 3) == 0:
            out = "Fizz"
        elif (number % 5) == 0:
            out = "Buzz"
        else:
            out = number
    else:
        out = "Error - Input is not an integer"
    return out
