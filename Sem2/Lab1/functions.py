# Script Name: functions.py
# Author: Conor Fox 119322236


def three_numbers(number_1, number_2, number_3):
    if number_1 == number_2 == number_3:
        return True
    else:
        return False


def seasons(number):
    seasons = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
    if isinstance(number, int):
        if number in seasons:
            return seasons[number]
        else:
            return "Number entered, "+str(number)+", is outside of input values"
    else:
        return "Input value must be a number"
