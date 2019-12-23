#!/usr/bin/python
########################################################################
# original code available at 'https://pythonspot.com/snake-with-pygame/'
#
# modification by jason quinlan j.quilan@cs.ucc.ie 2019
########################################################################

import pygame
import os
import time
from pygame.locals import *
from random import randint

windowWidthSize = 800
windowHeightsize = 600


class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self, x, y):
        self.reset(x, y)

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

    def reset(self, x, y):
        self.x = x * self.step
        self.y = y * self.step


class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 0

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.reset(length)

    def reset(self, length):
        self.length = length
        self.direction = 0
        self.x = [0]
        self.y = [0]
        self.updateCountMax = 2
        self.updateCount = 0
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[1] = 1*44
        self.x[2] = 2*44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            # print("snake lenght %d" % self.length)
            surface.blit(image, (self.x[i], self.y[i]))


class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False


class Score:
    ''' Add score to the screen '''
    # I need this for the font setup for score
    pygame.init()
    font = pygame.font.SysFont('impact', 20)
    text_color = [255, 255, 255]
    text_bg = [0, 0, 0]
    text_x = windowWidthSize / 9
    text_y = windowHeightsize - (windowHeightsize / 9)
    lastscore = -1
    score = 0
    playerName = ""
    game = ""

    def draw(self, surface, image):
        # if SCORE != self.lastscore:
        self.lastscore = self.score
        msg = "Game %d: Score: %d for Player %s" % (
            self.game, self.score, self.playerName)
        text_surface = self.font.render(
            msg, True, self.text_color, self.text_bg)
        surface.blit(text_surface, [self.text_x, self.text_y])

    def reset(self, score):
        self.score = score


class App:

    windowWidth = windowWidthSize
    windowHeight = windowHeightsize
    player = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3)
        self.apple = Apple(5, 5)
        self.score = Score()

    def on_init(self):
        # this is moved to Score class for font set up
        # pygame.init()
        self._display_surf = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        print(os.getcwd())
        self._image_surf = pygame.image.load(os.getcwd()+"/images/snake.png").convert()
        self._apple_surf = pygame.image.load(os.getcwd()+"/images/apple.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        # does snake eat apple?
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y,
                                     self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2, 9) * 44
                self.apple.y = randint(2, 9) * 44
                self.player.length = self.player.length + 1
                self.score.score = self.score.score + 1

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0], self.player.y[0],
                                     self.player.x[i], self.player.y[i], 40):
                '''
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0])
                      + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i])
                      + "," + str(self.player.y[i]) + ")")
                # exit(0)
                '''
                # lets get out of the game loop
                self._running = False
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.score.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def reset(self):
        self.player.reset(3)
        self.apple.reset(5, 5)
        self.score.reset(0)

    #  create the dictionary needed from the input lists
    def on_execute_list(self, numGames, player_names, player_values):
        # print("\nCreate Dictionary")
        playerResults = {}
        # print(playerResults)

        # for each player
        # set a counter
        i = 0
        # for each player in the name list
        for player in player_names:
            # set the initial value of the total score
            playerResults[player] = player_values[i]
            # increment our counter
            i += 1

        #  call the execute function with the dictionary
        self.on_execute(numGames, playerResults)

    def on_execute(self, numGames, playerResults):

        winner = [""] * numGames

        for i in range(numGames):
            for player, result in playerResults.items():

                if self.on_init() is False:
                    self._running = False

                # set the player name and game number
                self.score.playerName = player
                self.score.game = i + 1

                while(self._running):
                    pygame.event.pump()
                    keys = pygame.key.get_pressed()

                    if (keys[K_RIGHT]):
                        self.player.moveRight()

                    if (keys[K_LEFT]):
                        self.player.moveLeft()

                    if (keys[K_UP]):
                        self.player.moveUp()

                    if (keys[K_DOWN]):
                        self.player.moveDown()

                    if (keys[K_ESCAPE]):
                        self._running = False

                    self.on_loop()
                    self.on_render()

                    time.sleep(50.0 / 1000.0)

                # lets save the score for this user
                playerResults[player] += self.score.score

                # reset the running variable
                self._running = True
                self.reset()

            # who won this game?
            listOfKeys = [key for (key, value) in playerResults.items()]

            # this should work for any number of players
            maxScore = -1
            # go over the list and find the highest score
            for player1 in listOfKeys:
                # we only check if the value of player1 score is > maxScore
                # print("%s has a score of %d" % (player1, playerResults[player1]))
                if playerResults[player1] >= maxScore:
                    # get the second player
                    for player2 in listOfKeys:
                        # don't check the same player against themselves
                        if player1 != player2:
                            # if the player scores are the same
                            if playerResults[player1] == playerResults[player2]:
                                winner[i] = "Draw"
                                maxScore = playerResults[player1]
                                # print("winner %s" % winner[i])
                                # print("score %d" % playerResults[player1])
                                break
                            # if playerOne scored more
                            elif playerResults[player1] > playerResults[player2]:
                                winner[i] = player1
                                maxScore = playerResults[player1]
                                # print("winner %s" % winner[i])
                                # print("score %d" % playerResults[player1])
                            # if playerOne scored less
                            else:
                                winner[i] = player2
                                maxScore = playerResults[player2]
                                # print("winner %s" % winner[i])
                                # print("score %d" % playerResults[player2])

            if winner[i] == "Draw":
                print("Game %d is a tie" % (i+1))
            else:
                print("Game %d was won by %s" % (i+1, winner[i]))

            '''
            # this works for 2 players only
            player1 = listOfKeys[0]
            player2 = listOfKeys[1]
            if playerResults[player1] == playerResults[player2]:
                print("Game %d is a tie between %s and %s" %
                      (i+1, player1, player2))
                winner[i] = "Draw"
            elif playerResults[player1] < playerResults[player2]:
                print("Game %d was won by %s" % (i+1, player2))
                winner[i] = player2
            else:
                print("Game %d was won by %s" % (i+1, player1))
                winner[i] = player1

            '''

            # reset the scores for all players
            for player in listOfKeys:
                playerResults[player] = 0

            # check of we have a winner for best out of 'numGames'
            for player in listOfKeys:
                if winner.count(player) > numGames/2:
                    break

        # let's count how many times a player wins
        winner_count = {}
        maxCounter = 0
        # for each player
        for player, _ in playerResults.items():
            # store the number of times they won
            winner_count[player] = winner.count(player)
            # also store the max number of wins
            if winner_count[player] > maxCounter:
                maxCounter = winner_count[player]

        print(winner_count)
        print("maxCounter 1 : %d" % maxCounter)

        # let's see who won
        winnerName = ""
        maxCount = 0
        # for each player
        for player, result in winner_count.items():
            # let's see who and how many have the max count vlue
            if result == maxCounter:
                print(player)
                winnerName = player
                maxCount += 1

        print("maxCount 2 : %d" % maxCount)

        # if there is more than one winner, then it's a tie
        if maxCount > 1:
            print("It is a tie")
        else:
            # otherwise we have a winner :)
            print("The Game was won by %s" % (winnerName))

        '''
        # get the results for 2 players
        if winner.count(player2) == winner.count(player1):
            print("It is a tie between %s and %s" %
                  (player1, player2))
        elif winner.count(player2) > winner.count(player1):
            print("The Game was won by %s" % (player2))
        else:
            print("The Game was won by %s" % (player1))
        '''

        # stop the game
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute_list(1, ["Tim", "Tom"], [0, 0])
