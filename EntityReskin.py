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

img_x = 100
img_y = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EntityReskin")
clock = pygame.time.Clock()

test_image = pygame.image.load('test.jpg')


def set_color(img, mode): # removes 0 - red, 1 - green, 2 - blue, 3 - yellow
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel = img.get_at((x, y))
            if mode == 0:
                img.set_at((x,y), (0, pixel.g, pixel.b))
            elif mode == 1:
                img.set_at((x,y), (pixel.r, 0, pixel.b))
            elif mode == 2:
                img.set_at((x,y), (pixel.r, pixel.g, 0))
            else:
                img.set_at((x, y), (pixel.r, pixel.g, pixel.b))


def image(x, y):
    screen.blit(test_image, (x, y))


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():        # gets all the events which have occurred till now and keeps tab of them.
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                set_color(test_image, 0)
            elif event.key == pygame.K_g:
                set_color(test_image, 1)
            elif event.key == pygame.K_b:
                set_color(test_image, 2)
            elif event.key == pygame.K_y:
                set_color(test_image, 3)

    screen.fill(WHITE)
    image(img_x, img_y)
    pygame.display.flip()