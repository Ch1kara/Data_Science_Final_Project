import pygame
import sys

black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

def create_button(x, y, width, height, text):
    """Creates buttons that are highlighted when the cursor hovers over it"""
    # create base button rectangle
    button = pygame.Rect(x, y, width, height)

    # position of the mouse
    cursor_pos = pygame.mouse.get_pos()
    cursor_hover = button.collidepoint(cursor_pos)

    # makes outline of box gold if cursor is on it
    if cursor_hover:
        pygame.draw.rect(screen, white, button)
        pygame.draw.rect(screen, gold, button, 3)
    else:
        pygame.draw.rect(screen, white, button)
        pygame.draw.rect(screen, white, button, 3)

    # adds text to the box after everything else
    font = pygame.font.SysFont('squaresans', 18)
    text = font.render(f'{text}', True, black)
    text_rect = text.get_rect(center=button.center)
    screen.blit(text, text_rect)

    pygame.display.update()

    return button

def message(message):
    """Displays messages in game by creating objects"""
    # Blit and Load: https: // waylonwalker.com / pygame - image - load /
    # Fonts: https://nerdparadise.com/programming/pygame/part5

    pygame.draw.rect(screen, white, (10, 400, 520, 140))
    pygame.draw.rect(screen, black, (10, 400, 520, 140), 3)

    font = pygame.font.SysFont("squaresans", 25)
    text = font.render(message, True, black)

    # creates rectangle
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410

    # connecting the text with the rectangle as one object
    screen.blit(text, text_rect)
    # updates this portion of the screen
    pygame.display.update()


# Example usage
pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    create_button(100, 100, 200, 50, "Hype")
    message("Play again?")


