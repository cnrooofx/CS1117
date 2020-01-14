# Script Name: functions.py
# Author: Conor Fox 119322236


def three_numbers(number_1, number_2, number_3):
    if number_1 == number_2 == number_3:
        return True
    return False


def seasons(number):
    seasons = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
    if type(number) == int:
        if number in seasons:
            return seasons[number]
        return "Number entered, "+str(number)+", is outside of input values"
    return "Input value must be a number"


def grades(score):
    if type(score) == int:
        if score >= 0 and score <= 24:
            return "F"
        elif score >= 25 and score <= 39:
            return "E"
        elif score >= 40 and score <= 54:
            return "D"
        elif score >= 55 and score <= 69:
            return "C"
        elif score >= 70 and score <= 84:
            return "B"
        elif score >= 85 and score <= 100:
            return "A"
        return "The input numerical grade is outside the supported range."
    elif type(score) == str:
        grade = {"A": "85-100", "B": "70-84", "C": "55-69", "D": "40-54",
                 "E": "25-39", "F": "0-24"}
        if score in grade:
            return grade[score]
        return "The input letter grade is outside the supported range."
    return "Please enter an integer 0 - 100 or a letter A - F"


def slice_reverse(input_value):
    input_value = str(input_value)
    if input_value == input_value[::-1]:
        return True
    return False
