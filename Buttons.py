import pygame

screen_height = 1000
screen_width = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Test')

#Importing images
bulbasaur = pygame.image.load('bulbasaurfront.png').convert_alpha()
squirtle = pygame.image.load('squirtlefront.png').convert_alpha()

#Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.size = 150
    def set_sprite(self, orientation):
        """Grab the image of the pixelated Pokémon from the Pokémon API"""
        # Load the image into Pygame
        self.image = pygame.image.load(f"images/{self.name}{orientation}.png")
        # https: // www.pygame.org / docs / ref / image.html  # pygame.image.load



        # scales the image
        scale = self.size / self.image.get_width()
        nwidth = self.image.get_width() * scale
        nheight = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (nwidth, nheight))
    def draw(self):
        """Draws the button on the screen"""
        #get pos
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("Click")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

#Create buttons
Bulbasaur_button = Button(100,200, bulbasaur,5)
Squirtle_button = Button(600,200,squirtle,5)

run = True
while run:
    screen.fill((255, 87, 51))
    Bulbasaur_button.draw()
    Squirtle_button.draw()
    #Event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
    #Updates game window
    pygame.display.update()

pygame.quit()