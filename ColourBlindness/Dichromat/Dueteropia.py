import pygame
pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('Lizard.jpg').convert()


def Deuteropia(surface, filename):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            pixelValue = (pixel.r + pixel.b)/2
            surface.set_at((x, y), (pixel.r, pixelValue, pixel.b))
    pygame.image.save(surface, filename)


Deuteropia(my_surface, "Deuteropia.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
