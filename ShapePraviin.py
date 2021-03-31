import pygame
import random
from BlockPraviin import Block
from GameBoardPraviin import gameboardwidth
from GameBoardPraviin import gameboardheight
from GameBoardPraviin import activeBoardSpot
from GameBoardPraviin import activeBoardColour

SSHAPE = [(gameboardwidth / 2 - 1, 1),(gameboardwidth / 2 - 2, 1),(gameboardwidth / 2 - 1, 0),(gameboardwidth / 2, 0)]
SQUARE = [(gameboardwidth / 2, 0), (gameboardwidth / 2 + 1, 0), (gameboardwidth / 2, 1), (gameboardwidth / 2 + 1, 1)]
LINESHAPE = [(gameboardwidth / 2, 1), (gameboardwidth / 2, 0), (gameboardwidth / 2, 2), (gameboardwidth / 2, 3)]
LSHAPE = [(gameboardwidth / 2, 1), (gameboardwidth / 2, 0), (gameboardwidth / 2, 2), (gameboardwidth / 2 + 1, 2)]
ZSHAPE = [(gameboardwidth / 2, 0), (gameboardwidth / 2 - 1, 0), (gameboardwidth / 2, 1), (gameboardwidth / 2 + 1, 1)]
TSHAPE = [(gameboardwidth / 2, 0), (gameboardwidth / 2 - 1, 0), (gameboardwidth / 2 + 1, 0), (gameboardwidth / 2, 1)]
BW_LSHAPE = [(gameboardwidth / 2, 1), (gameboardwidth / 2, 0), (gameboardwidth / 2, 2), (gameboardwidth / 2 - 1, 2)]
ALLSHAPES = [SSHAPE, SQUARE, LINESHAPE, LSHAPE, ZSHAPE, TSHAPE, BW_LSHAPE]

BLACK = (0,0,0)
WHITE=(255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)
ORANGE = (255, 165, 0)
GREY = (169,169,169)
ALLCOLOURS = [ORANGE, MAGENTA, BLUE, YELLOW, RED, GREEN, TURQUOISE]

class Shape():
    def __init__ (self):
        randomNum = random.randrange(7)
        self.shape = ALLSHAPES[randomNum]
        self.numblocks = 4
        self.colour = ALLCOLOURS[randomNum]
        self.blocklist = []
        self.ghostblocklist = []
        self.active=True
        for i in range(self.numblocks):
            self.blocklist.append(Block(self.colour, self.shape[i][0], self.shape[i][1]))
            self.ghostblocklist.append(Block(self.colour, self.shape[i][0], self.shape[i][1]))

    def draw(self, screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen)

    def MoveLeft (self):
        Blocked = False
        for i in range (self.numblocks):
            if self.blocklist[i].gridXpos == 0 or activeBoardSpot[self.blocklist[i].gridXpos - 1][self.blocklist[i].gridYpos]:
                Blocked=True
        if Blocked == False:
            for i in range (self.numblocks):
                self.blocklist[i].gridXpos -= 1

    def MoveRight(self):
        Blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridXpos == gameboardwidth - 1 or activeBoardSpot[self.blocklist[i].gridXpos+ 1][self.blocklist[i].gridYpos]:
                Blocked = True
        if Blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridXpos += 1

    def falling(self):
        for i in range(self.numblocks):
            if self.blocklist[i].gridYpos == gameboardheight - 1 or activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos+1]:
                self.active = False
                self.hitBottom()
        if self.active == True:
            for i in range(self.numblocks):
                self.blocklist[i].gridYpos += 1

    def rotateCW(self):
        if self.shape != SQUARE:
            newBlockX = [0,0,0,0]
            newBlockY = [0,0,0,0]
            canRotate= True
            for i in range (self.numblocks):
                newBlockX[i] = -(self.blocklist[i].gridYpos - self.blocklist[0].gridYpos) + self.blocklist[0].gridXpos
                newBlockY[i] = (self.blocklist[i].gridXpos - self.blocklist[0].gridXpos) + self.blocklist[0].gridYpos
                if newBlockX[i]<0 or newBlockX[i]>=gameboardwidth-1:
                        canRotate = False
                elif newBlockY[i]>=gameboardheight-1 or newBlockY[i]<0:
                        canRotate = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canRotate = False
            if canRotate:
                for i in range (self.numblocks):
                    self.blocklist[i].gridXpos = newBlockX[i]
                    self.blocklist[i].gridYpos = newBlockY[i]

    def rotateCCW(self):
        if self.shape != SQUARE:
            newBlockX = [0,0,0,0]
            newBlockY = [0,0,0,0]
            canRotate= True
            for i in range (self.numblocks):
                newBlockX[i] = (self.blocklist[i].gridYpos - self.blocklist[0].gridYpos) + self.blocklist[0].gridXpos
                newBlockY[i] = -(self.blocklist[i].gridXpos - self.blocklist[0].gridXpos) + self.blocklist[0].gridYpos
                if newBlockX[i]<0 or newBlockX[i]>=gameboardwidth-1:
                        canRotate = False
                elif newBlockY[i]>=gameboardheight-1 or newBlockY[i]<0:
                        canRotate = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canRotate = False
            if canRotate:
                for i in range (self.numblocks):
                    self.blocklist[i].gridXpos = newBlockX[i]
                    self.blocklist[i].gridYpos = newBlockY[i]


    def drawnextshape(self,screen, x, y):
        for i in range(self.numblocks):
            pygame.draw.rect(screen, self.blocklist[i].colour, [self.blocklist[i].gridXpos*self.blocklist[i].size + x, self.blocklist[i].gridYpos *self.blocklist[i].size + y, self.blocklist[i].size -1, self.blocklist[i].size -1], 0)

    def drop(self):
        while self.active:
            for i in range(4):
                if self.blocklist[i].gridYpos == gameboardheight - 1 or activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos + 1]:
                    self.hitBottom()
            for i in range(4):
                if self.active:
                    self.blocklist[i].gridYpos += 1

    def drawGhostBlock(self, screen):
        for i in range(self.numblocks):
            self.ghostblocklist[i].gridXpos = self.blocklist[i].gridXpos
            self.ghostblocklist[i].gridYpos = self.blocklist[i].gridYpos
        done = False
        while not done:
            for i in range(4):
                if self.ghostblocklist[i].gridYpos < gameboardheight - 1:
                    self.ghostblocklist[i].gridYpos += 1
            for i in range(4):
                if self.ghostblocklist[i].gridYpos == gameboardheight - 1 or activeBoardSpot[self.ghostblocklist[i].gridXpos][self.ghostblocklist[i].gridYpos + 1]:
                    done = True
        for i in range(self.numblocks):
            self.ghostblocklist[i].ghostdraw(screen)

    def hitBottom(self):
        for i in range(self.numblocks):
            activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos] = True
            activeBoardColour[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos] = self.blocklist[i].colour
        self.active = False