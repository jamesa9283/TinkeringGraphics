import pygame

pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('GingerCat.jpg').convert()


def lessRed(surface=pygame.Surface((1, 1)), amount = float):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y),
                           pygame.Color(int(pixel.r * amount), pixel.g, pixel.b))


def lessGreen(surface=pygame.Surface((1, 1)), amount = float):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y),
                           pygame.Color(pixel.r, int(pixel.g * amount), pixel.b))


def lessBlue(surface=pygame.Surface((1, 1)), amount = float):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y),
                           pygame.Color(pixel.r, pixel.g, int(pixel.b * amount)))


amount = 0.5    # tinker with this value
lessRed(my_surface, amount)
lessGreen(my_surface, amount)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()