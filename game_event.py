import pygame
import sys
import random
def lineleft():
    plotpoints = [(200, 0), (50, 480)]
    pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
    pygame.display.flip()
def lineright():
    plotpoints = [(400, 0), (550,480)]
    pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
    pygame.display.flip()
def linemiddle():
    plotpoints = []
    x = 300
    for y in range(0, 480, 20):
        plotpoints.append([x, y])
        if len(plotpoints) == 2:
            pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
            plotpoints = []
    pygame.display.flip()
def loadcar(y):
    my_car = pygame.image.load('car.jpg')
    loc = [310, y]
    screen.blit(my_car, loc)
    pygame.display.flip()
def loadtext(x, y):
    textstr = 'location:' + str(x) + ',' + str(y)
    text_screen = my_font.render(textstr, True, (255, 0, 0))
    screen.blit(text_screen, (50, 50))
    pygame.display.flip()

pygame.init()
screencaption = pygame.display.set_caption('motorcycle race')
screen = pygame.display.set_mode([640, 480])
my_font = pygame.font.SysFont(None, 33)
screen.fill([255, 255, 255])
loadtext(310, 0)
lineleft()
lineright()
linemiddle()

looper = 480
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, [255, 255, 255], [310, looper, 40, 38], 0)
            pygame.draw.rect(screen, [255, 255, 255], [187, 50, 50, 33], 0)
            if event.key == pygame.K_UP:
                looper -= 20
                if looper < 0:
                    looper = 480
                loadcar(looper)
                loadtext(310, looper)
            if event.key == pygame.K_DOWN:
                looper += 20
                if looper >= 480:
                    looper = 0
                loadcar(looper)
                loadtext(310, looper)

