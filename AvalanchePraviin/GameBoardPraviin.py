import pygame
gameboardwidth = 12
gameboardheight = 20
class GameBoard():
    def __init__ (self, colour, blocksize):
        self.colour=colour
        self.multiplier = blocksize
    def draw (self, Screen):
        pygame.draw.rect(Screen, self.colour, [0,0, gameboardwidth*self.multiplier, gameboardheight * self.multiplier], 1)