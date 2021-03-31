import pygame
import random

GREY = (169,169,169)
gameboardwidth = 12
gameboardheight = 20
activeBoardSpot = [[0 for y in range(gameboardheight)] for x in range(gameboardwidth)]
activeBoardColour = [[0 for y in range(gameboardheight)] for x in range(gameboardwidth)]
#pygame.init()
#linesound = pygame.mixer.Sound("TetrisLine.mp3")

class GameBoard():
    def __init__(self, colour, blocksize):
        self.bordercolour = colour
        self.multiplier = blocksize
        self.score = 0
        self.numlines = 0
        self.templeveltracker = 0
        self.level = 1
        self.numslowtime = 2
        self.slowtimeon = False
        self.numswapshape = 2
        self.swapshapeon = False
        self.pause = False
        self.timer = 120
        self.garbageTimer = random.randrange(11) + 25
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                activeBoardSpot[i][j] = False
                activeBoardColour[i][j] = (0,0,0)

    def checkloss(self):
        for i in range(gameboardwidth):
            if activeBoardSpot[i][0]:
                return True
        return False

    def isCompleteLine(self, rowNum):
        for i in range (gameboardwidth):
            if activeBoardSpot[i][rowNum]== False:
                return False
        return True

    def clearFullRows(self):
        for j in range (gameboardheight):
            if self.isCompleteLine(j):
                self.score += 100
                self.timer += 7
                self.numlines += 1
                self.templeveltracker += 1
                #linesound.play()
                if self.templeveltracker == 10:
                    self.level += 1
                    if self.level % 2 == 0:
                        self.numslowtime += 1
                        self.numswapshape += 1
                    self.templeveltracker = 0
                for c in range(j, 1, -1):
                    for i in range (gameboardwidth):
                        activeBoardSpot[i][c] = activeBoardSpot[i][c-1]
                        activeBoardColour[i][c] = activeBoardColour[i][c - 1]
                for r in range(gameboardwidth):
                    activeBoardSpot[r][0] = False
                    activeBoardColour[r][0] = (0, 0, 0)

    def addGarbageLine(self):
        for c in range(1, gameboardheight - 1):
            for i in range(gameboardwidth):
                activeBoardSpot[i][c] = activeBoardSpot[i][c + 1]
                activeBoardColour[i][c] = activeBoardColour[i][c + 1]
        unfilledBlockNum = random.randrange(gameboardwidth)
        for k in range(gameboardwidth):
            if k != unfilledBlockNum:
                activeBoardSpot[k][gameboardheight - 1] = True
                activeBoardColour[k][gameboardheight - 1] = GREY
            else:
                activeBoardSpot[k][gameboardheight - 1] = False
                activeBoardColour[k][gameboardheight - 1] = (0, 0, 0)


    def draw(self, Screen, x, y):
        pygame.draw.rect(Screen, self.bordercolour, [x,y, gameboardwidth * self.multiplier, gameboardheight * self.multiplier], 1)
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                if activeBoardSpot[i][j]:
                    pygame.draw.rect(Screen, activeBoardColour[i][j], [i*self.multiplier, j*self.multiplier, self.multiplier - 1, self.multiplier - 1], 0)