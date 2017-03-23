import pygame
import sys
import random
def lineleft():
    plotpoints = [(200, 0), (50, 480)]
    pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
    #pygame.display.flip()
def lineright():
    plotpoints = [(400, 0), (550,480)]
    pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
    #pygame.display.flip()
def linemiddle():
    plotpoints = []
    x = 300
    for y in range(0, 480, 20):
        plotpoints.append([x, y])
        if len(plotpoints) == 2:
            pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
            plotpoints = []
    #pygame.display.flip()
def loadcar(y):
    my_car = pygame.image.load('car.jpg')
    loc = [310, y]
    screen.blit(my_car, loc)
    pygame.display.flip()

pygame.init()
screencaption = pygame.display.set_caption('motorcycle race')
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 0])
lineleft()
lineright()
linemiddle()

clock = pygame.time.Clock()
looper = 480
speed = -300 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    while True:
        pygame.time.delay(10)
        pygame.draw.rect(screen, [255, 255, 0], [310, looper, 40, 38], 0)
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0
        print time_passed_seconds
        distance_moved = looper + time_passed_seconds * speed
        looper = distance_moved
        if looper > 480 or looper < 0:
            looper = 480
        loadcar(looper)
        






