import pygame
import sys

WIDTH, HEIGHT = SIZE = (640, 480)
FPS = 60

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def ColourDistance(colourA: (int, int, int), colourB: (int, int, int)) -> float:
    return ((colourA[0]-colourB[0])**2 + (colourA[1]-colourB[1])**2 + (colourA[2]-colourB[2])**2)**0.5


print(ColourDistance(WHITE, BLACK))

sys.exit(1)


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GAMENAME")
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()