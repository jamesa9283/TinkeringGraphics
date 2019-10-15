import pygame

pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('GingerCat.jpg').convert()


def ColourBlindness(surface):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            pixelValue = (pixel.b + pixel.b) / 2
            surface.set_at((x, y), (pixel.r, pixelValue, pixelValue))


amount = 0.75  # tinker with this value
ColourBlindness(my_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
