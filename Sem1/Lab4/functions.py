# ScriptName: functions.py
# Author: Conor Fox 119322236


def seasons(number):
    """
    Takes number between 1 and 4 and displays corresponding season
    number -- Between 1 and 4
    """
    seasons_list = ["Spring", "Summer", "Autumn", "Winter"]

    if number == 1:
        out = seasons_list[3]
    elif number == 2:
        out = seasons_list[0]
    elif number == 3:
        out = seasons_list[1]
    elif number == 4:
        out = seasons_list[2]
    else:
        out = "Please enter an integer between 1 and 4"
    return out


def grades(score):
    """
    Gives grade based on test score
    score -- Test score between 0 and 100 or grade between A and F
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
            out = "The input numerical grade is outside the supported range."

    elif isinstance(score, str):
        if score == "F":
            out = "0-24"
        elif score == "E":
            out = "25-39"
        elif score == "D":
            out = "40-54"
        elif score == "C":
            out = "55-69"
        elif score == "B":
            out = "70-84"
        elif score == "A":
            out = "85-100"
        else:
            out = "The input letter grade is outside the supported range."
    else:
        out = "Please enter an integer 0 - 100 or a letter A - F"
    return out


def fizz_buzz(number, divisor_1, divisor_2):
    """
    Like game of FizzBuzz, if number is a multiple of 'divisor_1'
    prints Fizz, if number is a multiple of 'divisor_2' prints Buzz
    and if number is a multiple of both prints FizzBuzz.
    number -- Number to be inputted
    divisor_1 -- First number to be used as divisor (Fizz)
    divisor_2 -- Second number to be used as divisor (Buzz)
    """
    if isinstance(number, int):
        if (number % divisor_1) == 0 and (number % divisor_2) == 0:
            out = "FizzBuzz"
        elif (number % divisor_1) == 0:
            out = "Fizz"
        elif (number % divisor_2) == 0:
            out = "Buzz"
        else:
            out = number
    else:
        out = "Input is not an integer"
    return out


def slice_reverse(input_value):
    """
    If the input value is a palindrome (spelt the same forwards and backwards)
    then output is true, otherwise false.
    input_value -- value to check if palindrome
    """
    input_value = str(input_value)
    input_value.lower()
    if input_value == input_value[::-1]:
        out = True
    else:
        out = False
    return out


def add_to_list(value, the_list):
    """
    Compares a value to a list. If the value is not in the list, it is added
    and the list is sorted. If the value isn't in the list then it is just
    sorted and printed.
    value -- Value to be compared
    the_list -- List to check with value
    """
    if value not in the_list:
        the_list.append(value)
    the_list.sort()
    return the_list
