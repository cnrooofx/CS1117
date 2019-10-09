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
