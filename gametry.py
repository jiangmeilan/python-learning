import pygame
import sys
import random
def lineleft():
    plotpoints = []
    lst = [0, 640]
    for x in lst:
        y = -5 * x + 1000
        plotpoints.append([x, y])
    pygame.draw.lines(screen, [0, 0, 0], False, plotpoints, 5)
    pygame.display.flip()
def lineright():
    plotpoints = []
    lst = [0, 640]
    for x in lst:
        y = 5 * x - 2000
        plotpoints.append([x, y])
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

pygame.init()
clock = pygame.time.Clock()
print clock.tick()
pygame.time.delay(20)
print clock.tick()
pygame.time.delay(10)
print clock.tick()
pygame.time.delay(3)
print clock.tick()
