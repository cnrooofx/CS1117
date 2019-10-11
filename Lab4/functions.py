# ScriptName: functions.py
# Author: Conor Fox 119322236


def seasons(number):
    """
    Takes number between 1 and 4 and displays corresponding season
    number -- Between 1 and 4
    """
    seasons_list = ["Spring", "Summer", "Autumn", "Winter"]

    if number == 1:
        print(seasons_list[3])
    elif number == 2:
        print(seasons_list[0])
    elif number == 3:
        print(seasons_list[1])
    elif number == 4:
        print(seasons_list[2])
    else:
        print("Error - please enter an integer between 1 and 4")


def grades(score):
    """
    Gives grade based on test score
    score -- Test score between 0 and 100 or grade between A and F
    """
    if type(score) == int:
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
            print("The input numerical grade is outside the supported range.")

    elif type(score) == str:
        if score == "F":
            print("0-24")
        elif score == "E":
            print("25-39")
        elif score == "D":
            print("40-54")
        elif score == "C":
            print("55-69")
        elif score == "B":
            print("70-84")
        elif score == "A":
            print("85-100")
        else:
            print("The input letter grade is outside the supported range.")
    else:
        print("Error - please enter an integer 0 - 100 or a letter A - F")


def fizz_buzz(number, divisor_1, divisor_2):
    """
    Like game of FizzBuzz, if number is a multiple of 'divisor_1'
    prints Fizz, if number is a multiple of 'divisor_2' prints Buzz
    and if number is a multiple of both prints FizzBuzz.
    number -- Number to be inputted
    divisor_1 -- First number to be used as divisor
    divisor_2 -- Second number to be used as divisor
    """
    if type(number) == int:
        if (number % divisor_1) == 0 and (number % divisor_2) == 0:
            print("FizzBuzz")
        elif (number % divisor_1) == 0:
            print("Fizz")
        elif (number % divisor_2) == 0:
            print("Buzz")
        else:
            print(number)
    else:
        print("Error - Input is not an integer")


def slice_reverse(input_value):
    """
    If the input value is a palindrome (spelt the same forwards and backwards)
    then output is true, otherwise false.
    input_value -- value to check if palindrome
    """
    input_value = str(input_value)
    input_value.lower()
    if input_value == input_value[::-1]:
        print("True")
    else:
        print("False")


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
    print(the_list)
