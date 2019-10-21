import sys
import math
import pygame

WIDTH = 800
HEIGHT = 640
FPS = 60

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TinkeringGraphics")
clock = pygame.time.Clock()


def getColourDistance(colourA, colourB):
    distance = math.sqrt((colourA[0] - colourB[0]) ** 2 + (colourA[1] - colourB[1])**2 + (colourA[2] - colourB[2])**2)
    print(distance)
    return distance


def closeEnough(colourA, colourB):
    if getColourDistance(colourA, colourB) < 50.0:
        print("close")
        return True
    else:
        print("not close")
        return False


closeEnough(WHITE, BLACK)

# Game loop
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
