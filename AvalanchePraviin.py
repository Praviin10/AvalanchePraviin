import pygame
import time
import random
from BlockPraviin import Block
from GameBoardPraviin import GameBoard
from GameBoardPraviin import gameboardheight
from GameBoardPraviin import gameboardwidth
from GameBoardPraviin import activeBoardSpot
from ShapePraviin import Shape
#from Multiplayer import drawMultiplayer

BLACK = (0,0,0)
WHITE=(255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)
GREY = (192,192,192)

if __name__=="__main__":
    pygame.init()
    pygame.mixer.init()
    # pygame.mixer.music.load("Tetris.mp3")
    # pygame.mixer.music.play(-1)
    myfont = pygame.font.Font("freesansbold.ttf", 30)
    timefont = pygame.font.Font("freesansbold.ttf", 50)
    HSfont = pygame.font.Font("freesansbold.ttf", 20)
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche-By:Praviin")
    shape = Shape()
    nextshape = Shape()
    gameboard = GameBoard(WHITE, 25)
    gameboard2 = GameBoard(WHITE, 25)
    namelist = [0 for y in range(5)]
    scorelist = [0 for y in range(5)]
    done = False
    started = False
    modeSelect = 0
    gameOverOn = False
    name = ""
    delay = 0
    slowtimedelay = 0

def multiplaerSize():
    size = (1000,600)
    screen = pygame.display.set_mode(size)

def KeyCheck():
    if event.key == pygame.K_p:
        gameboard.pause = not gameboard.pause
    if gameboard.pause == False:
        if event.key == pygame.K_LEFT:
            shape.MoveLeft()
        elif event.key == pygame.K_RIGHT:
            shape.MoveRight()
        elif event.key == pygame.K_d:
            shape.falling()
        elif event.key == pygame.K_UP:
            shape.rotateCW()
        elif event.key == pygame.K_DOWN:
            shape.rotateCCW()
        elif event.key == pygame.K_SPACE:
            gameboard.score+=gameboardheight - shape.blocklist[0].gridYpos
            shape.drop()
        elif event.key == pygame.K_t and gameboard.numslowtime>0:
            gameboard.numslowtime -= 1
            gameboard.slowtimeon = True
        elif event.key == pygame.K_y and gameboard.numswapshape>0:
            gameboard.numswapshape -= 1
            gameboard.swapshapeon = True

def drawMultiplayer():
    screen.fill(BLACK)
    shape.draw(screen)
    nextshape.drawnextshape(screen,250, 150)
    gameboard.draw(screen, 0, 0)
    gameboard2.draw(screen, 500, 0)
    shape.drawGhostBlock(screen)
    linetext = myfont.render("Lines: " + str(gameboard.numlines), 1, WHITE)
    screen.blit(linetext, (330, 400))
    nextshapetext = myfont.render("Next: ", 1, WHITE)
    screen.blit(nextshapetext, (330, 50))
    pygame.draw.rect(screen, WHITE, [330, 100, 6 * shape.blocklist[0].size, 6 * shape.blocklist[0].size], 1)
    poweruptext = myfont.render("Power Ups: ", 1, WHITE)
    screen.blit(poweruptext, (50, 525))
    slowtimeimage = pygame.image.load("clock.png")
    screen.blit(slowtimeimage, (250, 515))
    numswapshapetext = myfont.render(" x" + str(gameboard.numswapshape), 1, WHITE)
    screen.blit(numswapshapetext, (435, 525))
    swapshapeimage = pygame.image.load("swap.png")
    screen.blit(swapshapeimage, (375, 515))
    playernametext = myfont.render("Player: " + name, 1, WHITE)
    screen.blit(playernametext, (515, 525))
    pygame.display.flip()

def drawScreen():
    screen.fill(BLACK)
    shape.draw(screen)
    nextshape.drawnextshape(screen, 320, 150)
    gameboard.draw(screen,0,0)
    shape.drawGhostBlock(screen)
    scoretext = myfont.render("Score: " + str(gameboard.score),1, WHITE)
    screen.blit(scoretext,(400,350))
    linetext = myfont.render("Lines: " + str(gameboard.numlines),1, WHITE)
    screen.blit(linetext,(400,400))
    leveltext = myfont.render("Level: " + str(gameboard.level),1, WHITE)
    screen.blit(leveltext,(400,300))
    nextshapetext = myfont.render("Next: ", 1, WHITE)
    screen.blit(nextshapetext, (400, 50))
    pygame.draw.rect(screen, WHITE, [400,100,6*shape.blocklist[0].size, 6*shape.blocklist[0].size],1)
    poweruptext = myfont.render("Power Ups: ", 1, WHITE)
    screen.blit(poweruptext,(50, 525))
    numslowtimetext = myfont.render(" x" + str(gameboard.numslowtime), 1, WHITE)
    screen.blit(numslowtimetext,(310, 525))
    slowtimeimage = pygame.image.load("clock.png")
    screen.blit(slowtimeimage, (250, 515))
    numswapshapetext = myfont.render(" x" + str(gameboard.numswapshape), 1, WHITE)
    screen.blit (numswapshapetext,(435, 525))
    swapshapeimage = pygame.image.load("swap.png")
    screen.blit(swapshapeimage, (375, 515))
    highscoretext = myfont.render("High Scores", 1, WHITE)
    screen.blit(highscoretext, (575, 50))
    pygame.draw.rect(screen, WHITE, [575, 100, 200, 400], 1)
    playernametext = myfont.render("Player: " + name, 1, WHITE)
    screen.blit(playernametext, (515, 525))
    if modeSelect == 2:
        timertext = myfont.render("Time: " + str(gameboard.timer), 1, WHITE)
        screen.blit(timertext, (400, 450))
        if gameboard.timer <= 5:
            bigtimetext = timefont.render(str(gameboard.timer), 1, WHITE)
            screen.blit(bigtimetext, (145, 200))
    if gameboard.pause == True:
        pausetext = myfont.render("Paused", 1, WHITE)
        screen.blit(pausetext, (100, 200))
    for i in range(5):
        HSnametext = HSfont.render(str(namelist[i]), 1, WHITE)
        HSscoretext = HSfont.render(str(scorelist[i]), 1, WHITE)
        screen.blit(HSnametext, (580, i * 25 + 125))
        screen.blit(HSscoretext, (700, i * 25 + 125))
    if modeSelect == 1:
        HSfile = open("HighScores.txt", "r")
        for i in range(5):
            namelist[i] = HSfile.readline().rstrip("\n")
        for i in range(5):
            scorelist[i] = HSfile.readline().rstrip("\n")
        HSfile.close()
    elif modeSelect == 2:
        HSfile2 = open("HighScores2.txt", "r")
        for i in range(5):
            namelist[i] = HSfile2.readline().rstrip("\n")
        for i in range(5):
            scorelist[i] = HSfile2.readline().rstrip("\n")
        HSfile2.close()
    else:
        HSfile3 = open("HighScores3.txt", "r")
        for i in range(5):
            namelist[i] = HSfile3.readline().rstrip("\n")
        for i in range(5):
            scorelist[i] = HSfile3.readline().rstrip("\n")
        HSfile3.close()
    pygame.display.flip()

def checkHighScores():
    newhighscore = False
    tempnamelist = [0 for y in range(5)]
    tempscorelist = [0 for y in range(5)]
    for i in range(5):
        if gameboard.score > int(scorelist[i]) and newhighscore == False:
            newhighscore = True
            tempscorelist[i] = gameboard.score
            tempnamelist [i] = name
        elif newhighscore == True:
            tempscorelist[i] = scorelist[i-1]
            tempnamelist[i] = namelist[i-1]
        else:
            tempscorelist[i] = scorelist[i]
            tempnamelist[i] = namelist[i]
    for i in range(5):
        scorelist[i] = tempscorelist[i]
        namelist[i] = tempnamelist[i]
    if modeSelect == 1:
        HSfile = open("HighScores.txt", "w")
        for i in range(5):
            HSfile.write(namelist[i] + "\n")
        for i in range(5):
            HSfile.write(str(scorelist[i]) + "\n")
        HSfile.close()
    elif modeSelect == 2:
        HSfile2 = open("HighScores2.txt", "w")
        for i in range(5):
            HSfile2.write(namelist[i] + "\n")
        for i in range(5):
            HSfile2.write(str(scorelist[i]) + "\n")
        HSfile2.close()
    else:
        HSfile3 = open("HighScores3.txt", "w")
        for i in range(5):
            HSfile3.write(namelist[i] + "\n")
        for i in range(5):
            HSfile3.write(str(scorelist[i]) + "\n")
        HSfile3.close()

while not started:
    titlescreen = pygame.image.load("Backdrop.png")
    enterednametext = myfont.render("Please Enter Name", 1, WHITE)
    nametext = myfont.render(name,1, WHITE)
    screen.blit(enterednametext,(250,200))
    screen.blit(nametext, (300, 250))
    pygame.display.flip()
    screen.blit(titlescreen, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            started = True
        if event.type == pygame.KEYDOWN:
            if event.key >= 33 and event.key <=126 and len(name)<10:
                name = name + chr(event.key)
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            if event.key == pygame.K_RETURN:
                started = True
                if name == "":
                    name = "Player1"

while modeSelect == 0:
    modetext = myfont.render("Select your Mode:", 1, WHITE)
    modetext2 = myfont.render("Normal - 1, Time Attack - 2 , Garbage Line - 3", 1, WHITE)
    modetext3 = myfont.render("Multiplayer - 4", 1, WHITE)
    pygame.display.flip()
    screen.blit(modetext, (250, 200))
    screen.blit(modetext2, (75, 250))
    screen.blit(modetext3, (275, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            modeSelect = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                modeSelect = 1
            if event.key == pygame.K_2:
                modeSelect = 2
            if event.key == pygame.K_3:
                modeSelect = 3
            if event.key == pygame.K_4:
                modeSelect = 4

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            KeyCheck()
    delay += 1
    if delay >= 10 and gameboard.pause == False:
        shape.falling()
        if modeSelect == 2:
            gameboard.timer -= 1
        elif modeSelect == 3:
            gameboard.garbageTimer -= 1
        delay = 0
    if gameboard.timer <= 0:
        gameOverOn = True
    elif gameboard.garbageTimer<= 0:
        gameboard.addGarbageLine()
        gameboard.garbageTimer = random.randrange(11) + 25
    if gameboard.swapshapeon:
        shape = nextshape
        nextshape = Shape()
        gameboard.swapshapeon = False
    if gameboard.slowtimeon:
        slowtimedelay += 1
        if slowtimedelay >= 50:
            slowtimedelay = 0
            gameboard.slowtimeon = False
    if shape.active == False:
        gameboard.clearFullRows()
        shape = nextshape
        nextshape = Shape()
    if gameboard.checkloss() or gameboard.timer == 0:
        checkHighScores()
        gameboard = GameBoard(WHITE, shape.blocklist[0].size)
        shape = Shape()
        nextshape = Shape()
        gameOverScreen = pygame.image.load("GameOver.png")
        screen.blit(gameOverScreen,(0, 0))
        pygame.display.flip()
        time.sleep(5)
    if modeSelect == 4:
        drawMultiplayer()
        multiplaerSize()
    else:
        drawScreen()
    if 0.11 - gameboard.level*0.01 >= 0:
        time.sleep(0.11 - gameboard.level*0.01 + gameboard.slowtimeon*0.1)