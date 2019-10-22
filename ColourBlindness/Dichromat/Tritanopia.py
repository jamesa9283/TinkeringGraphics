# no sensitivity to blue light

import pygame
pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('Lizard.jpg').convert()


def Tritanopia(surface, filename):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            # averages red and green light
            pixelValue = (pixel.r + pixel.g)/2
            # replaces blue light with averaged red and green
            surface.set_at((x, y), (pixel.r, pixel.g, pixelValue))
    pygame.image.save(surface, filename)


Tritanopia(my_surface, "Tritanopia.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
