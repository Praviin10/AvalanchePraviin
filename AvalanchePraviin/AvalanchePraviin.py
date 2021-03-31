import pygame
from BlockPraviin import Block
from GameBoardPraviin import GameBoard
BLACK = (0,0,0)
WHITE=(255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)
if __name__=="__main__":
    pygame.init()
    size=(800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche-By:Praviin")
    block = Block(BLACK, 200, 120)
    gameboard = GameBoard (WHITE, block.size)
    done= False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    block.xpos -=10
                elif event.key ==pygame.K_RIGHT:
                    block.xpos +=10
                elif event.key ==pygame.K_DOWN:
                    block.ypos +=10
                elif event.key ==pygame.K_UP:
                    block.ypos -=10
        screen.fill(RED)
        block.draw (screen)
        gameboard.draw (screen)
        pygame.display.flip()