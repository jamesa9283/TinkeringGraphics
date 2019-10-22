# reduced sensitivity of blue light
# code written by James Arthur

import pygame
pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('Lizard.jpg').convert()


def Tritanomaly(surface, filename):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            # averaged blue and red light
            pixelValue = (pixel.b + pixel.r)/2
            # replaces blue with averaged blue and red light
            surface.set_at((x, y), (pixel.r, pixel.g, pixelValue))
    pygame.image.save(surface, filename)


Tritanomaly(my_surface, "tritanomaly.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
