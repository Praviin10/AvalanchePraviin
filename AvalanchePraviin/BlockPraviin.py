import pygame
class Block():
    def __init__ (self, colour, xpos, ypos):
        self.colour = colour
        self.xpos = xpos
        self.ypos = ypos
        self.size = 25
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour,[self.xpos, self.ypos, self.size, self.size], 0)