#!/usr/bin/python
# comments in Python, irrespective of verison
from game import App

"""
In this lab, I want you to write the code to call the Python Game
1   the game should ask how many players want to play?
    read input, convert to int, catch problems
2   the game will ask how many games you want (best out of)?
    read input, convert to int, make sure input is an odd number, \
    catch problems
#   '\' is used to spread the print out over multiple lines :)
3   the game asks for the name of each player and creates a \
    list or dictionary to store results
4   You must write the code.
"""


'''
#################################################
                    FUNCTIONS
#################################################
'''


def getIntegerInput(question):
    '''
    get an number value as input from the user - return an integer
    '''
    return int(input(str(question)+": "))


def getStringInput(question):
    '''
    get a string input from the user
    '''
    return input(str(question)+": ")


def getNumberPlayers():
    '''
    get the number of players
    '''
    return getIntegerInput("How many players?")


def getNumberGames():
    '''
    get the number of games
    '''
    num_games = getIntegerInput("How many games (best out of)?")
    return oddNumberGame(num_games)


def oddNumberGame(numGamesInput):
    '''
    make sure the number of games input is an odd, positive number
    '''
    if numGamesInput > 0:
        if numGamesInput % 2 == 0:
            numGamesInput -= 1
        return numGamesInput
    return 1


def main():
    # OUR MAIN FUNCTION
    '''
    #################################################
            GET NUMBER OF USERS AND GAMES
    #################################################
    '''

    num_players = getNumberPlayers()

    numGames = getNumberGames()

    '''
    #################################################
                GET NAMES OF USERS
    #################################################
    '''

    # lists
    '''
    create a list of initial player score values
    create a list of player names - asking the user for their names

    to call the game using lists uncomment these next 2 lines:
    theApp = App()
    theApp.on_execute_list(numGames, player_names, player_values)
    '''

    # dictionary
    '''
    create a dictionary
    create a dictionary of players names - asking the user for their names,
    as keys with the initial player score values, as values
    '''
    player_dictionary = {}
    initial_score = 0
    if num_players <= 1:
        player_dictionary["Player 1"] = getStringInput("What is your name")
        print(player_dictionary)
    else:
        i = 1
        while i < num_players+1:
            question = "Player "+str(i)+", What is your name?: "
            player_dictionary[getStringInput(question)] = initial_score
            i += 1
    '''
    to call the game using a dictionary uncomment these next 2 lines:
    '''
    theApp = App()
    theApp.on_execute(numGames, player_dictionary)


'''
THIS IS HOW WE START THE PROGRAM
'''
if __name__ == '__main__':
    main()
