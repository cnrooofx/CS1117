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
    score -- Test score between 0 and 100
    """
    if str(type(score)) == "<class 'int'>":
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

    elif str(type(score)) == "<class 'str'>":
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
        print("Error - please enter an integer between 0 and 100 or a letter between A and F")
