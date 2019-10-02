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
    if num1 == num2 and num2 == num3:
        print("True")
    else:
        print("False")


def seasons(number):
    """
    Takes number between 1 and 4 and displays corresponding season
    number -- Between 1 and 4
    """
    if number == 1:
        print("Spring")
    elif number == 2:
        print("Summer")
    elif number == 3:
        print("Autumn")
    elif number == 4:
        print("Winter")
    else:
        print("Error please enter an integer between 1 and 4")


def grades(score):
    """
    Gives grade based on test score
    score -- Test score between 0 and 100
    """
    if score >= 0 and score <= 24:
        print("F")
    elif score >= 25 and score <= 39:
        print("E")
    elif score >= 40 and score <= 54:
        print("D")
    elif score >= 55 and score <= 69:
        print("C")
    elif score >= 70 and score <= 84:
        print("B")
    elif score >= 85 and score <= 100:
        print("A")
    else:
        print("X")


def equal_numbers(num1, num2):
    if num1 == num2:
        square_root = math.sqrt(num1)
        print("The square root of %d is %d" % (int(num1), int(square_root)))
    else:
        square_num1 = num1 ** 2
        square_num2 = num2 ** 2

        print("\"%d\" squared is \"%d\" and \"%d\" squared is \"%d\"" % (num1, square_num1, num2, square_num2))


def fizz_buzz(number):
    """
    Like game of FizzBuzz, if number is a multiple of 3 prints Fizz, if number is a multiple of 5 prints Buzz and if number is a multiple of both prints FizzBuzz
    number -- Number to be inputted
    """
    if (number % 5) == 0 and (number % 3) == 0:
        print("FizzBuzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")
    else:
        print(number)
