import pygame
pygame.init()

# screen size and title at the top
screen = pygame.display.set_mode((750,500))
pygame.display.set_caption("Pokemon")

# defining colors needed for the future
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

run = True

while run:
    # event.get() for loop should be at the start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))

    # display.update() should be at the end
    pygame.display.update()
pygame.quit()