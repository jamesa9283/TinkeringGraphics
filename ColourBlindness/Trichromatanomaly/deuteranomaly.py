# reduced sensitivity to green light

import pygame
pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('Lizard.jpg').convert()


def TriColourBlindness(surface, filename):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            # averaged green and blue light
            pixelValue = (pixel.g + pixel.b)/2
            # replaces green with averaged green and blue light
            surface.set_at((x, y), (pixel.r, pixelValue, pixel.b))
    pygame.image.save(surface, filename)


TriColourBlindness(my_surface, "deuteranomaly.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
