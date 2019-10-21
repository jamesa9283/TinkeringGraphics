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
pygame.display.set_caption("EntityReskin")
clock = pygame.time.Clock()

test_image = pygame.image.load('test.jpg')


def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a  # Preserve the alpha value.
            img.set_at((x, y), color)  # Set the color of the pixel.


def image(x, y):
    screen.blit(test_image, (x, y))


img_x = 100
img_y = 100

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():        # gets all the events which have occurred till now and keeps tab of them.
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                set_color(test_image, pygame.Color(0, 0, 255))
            elif event.key == pygame.K_g:
                set_color(test_image, pygame.Color(0, 255, 0))
            elif event.key == pygame.K_b:
                set_color(test_image, pygame.Color(255, 0, 0))
            elif event.key == pygame.K_y:
                set_color(test_image, pygame.Color(255, 255, 0))

    screen.fill(WHITE)
    image(img_x, img_y)
    pygame.display.flip()