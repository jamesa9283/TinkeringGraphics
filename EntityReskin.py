import pygame
import math

WIDTH = 800
HEIGHT = 640
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (255, 255, 0)

CHROMA_KEY = GREEN  # this is the green that covers the armor pieces to be replaced with a "TEAM COLOUR"

img_x = 100
img_y = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Entity Reskinning")
clock = pygame.time.Clock()

test_image = pygame.image.load('armor.jpg')


def set_color(mode):  # replaces the chroma key with 0 - red, 1 - black, 2 - blue, 3 - yellow
    img = test_image
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel = img.get_at((x, y))
            if get_colour_distance(pixel) < 50:  # if the colour is close enough to the chroma key it will get replaced.
                if mode == 0:
                    img.set_at((x, y), RED)
                elif mode == 1:
                    img.set_at((x, y), BLACK)
                elif mode == 2:
                    img.set_at((x, y), BLUE)
                else:
                    img.set_at((x, y), YELLOW)
    save(img, mode)


def image(x, y):
    screen.blit(test_image, (x, y))


def save(surface, mode):
    pygame.image.save(surface, str(mode) + '_armor.jpg')


def get_colour_distance(pixel):
    distance = math.sqrt((CHROMA_KEY[0] - pixel[0]) ** 2 + (CHROMA_KEY[1] - pixel[1])**2 + (CHROMA_KEY[2] - pixel[2])**2)
    return distance


# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():  # gets all the events which have occurred till now.
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                set_color(0)
            elif event.key == pygame.K_g:
                set_color(1)
            elif event.key == pygame.K_b:
                set_color(2)
            elif event.key == pygame.K_y:
                set_color(3)

    screen.fill(WHITE)
    image(img_x, img_y)
    pygame.display.flip()