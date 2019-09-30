#  Script Name : rugby_world_cup.py
#  Author: Conor Fox 119322236


def rugby():
    '''
    Takes two rugby teams in world cup and displays scores in a table.
    '''
    team1 = str(input("What is the name of the first team: "))
    team2 = str(input("What is the name of the second team: "))

    tries_for_team1 = int(input("How many tries for " + team1 + ":"))
    tries_for_team2 = int(input("How many tries for " + team2 + ":"))

    points_team1 = int(input("How many converted/penalties for " + team1 + ":"))
    points_team2 = int(input("How many converted/penalties for " + team2 + ":"))

    score_team1 = tries_for_team1 + points_team1
    score_team2 = tries_for_team2 + points_team2

    print("      Team \t\t Tries \t\t Points \t Total Score \n\n", "-------------------------------------------------------------------", "\n")

    print("%10.10s \t %8.d \t %8.d \t %8.d" % (team1, tries_for_team1, points_team1, score_team1))
    print("%10.10s \t %8.d \t %8.d \t %8.d" % (team2, tries_for_team2, points_team2, score_team2))
    print()


def player():
    '''
    Asks for player name and age in days and converts to years and days.
    '''
    player_name = str(input("What is the player's name: "))
    player_name = player_name.lower()
    player_name = player_name.capitalize()

    days_old = int(input("How many days old is " + player_name + ": "))

    years_old = int((days_old/365))

    remaining_days = days_old - (365 * years_old)

    print(player_name + " is " + str(years_old) + " years and " + str(remaining_days) + " days old.")
    print()


def main():
    # rugby()
    player()


if __name__ == "__main__":
    main()
