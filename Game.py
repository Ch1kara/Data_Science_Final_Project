import pygame
from pygame.locals import *
import sys
import time
import random as rand

pygame.init()
clock = pygame.time.Clock()

# screen size and title at the top
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Game Adaptation")

# defining colors needed for the future
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# Base set of Pokémon from before, but eventually use json to scrape Pokémon data from Pokémon API
MOVES_DICTIONARY = {
    'Scratch':
        {
            'name': 'Scratch',
            'power': 40,
            'type': 'Normal',
            'super effective against': ['N/A'],
            'not very effective against': ['Rock', 'Steel']
        },
    'Tackle':
        {
            'name': 'Tackle',
            'power': 40,
            'type': 'Normal',
            'super effective against': ['N/A'],
            'not very effective against': ['Rock', 'Steel']
        },
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'],
              'not very effective against': ['Rock', 'Steel']},
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'],
             'not very effective against': ['Rock', 'Steel']},
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'],
                    'not very effective against': ['Rock', 'Steel']},
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'],
              'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire',
                  'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'],
                  'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'],
               'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water',
                 'super effective against': ['Fire', 'Ground', 'Rock'],
                 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric',
                      'super effective against': ['Water', 'Flying'],
                      'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric',
                    'super effective against': ['Water', 'Flying'],
                    'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass',
                  'super effective against': ['Water', 'Ground', 'Rock'],
                  'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass',
                     'super effective against': ['Water', 'Ground', 'Rock'],
                     'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice',
                  'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'],
                  'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']},
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting',
                    'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
                    'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']},
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground',
                   'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
                   'not very effective against': ['Grass', 'Bug']},
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying',
                    'super effective against': ['Grass', 'Fighting', 'Bug'],
                    'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'],
             'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic',
                  'super effective against': ['Fighting', 'Poison'],
                  'not very effective against': ['Psychic', 'Steel']},
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug',
                  'super effective against': ['Grass', 'Psychic', 'Dark'],
                  'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock',
                   'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'],
                   'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock',
                   'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'],
                   'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'],
             'not very effective against': ['Dark']},
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'],
                'not very effective against': ['Steel']},
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'],
               'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'],
             'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel',
                     'super effective against': ['Ice', 'Rock', 'Fairy'],
                     'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']},
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'],
             'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']},
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic',
                    'super effective against': ['Fighting', 'Poison'],
                    'not very effective against': ['Psychic', 'Steel']},
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'],
                  'not very effective against': ['Rock', 'Steel']},
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'],
                    'not very effective against': ['Rock', 'Steel']},
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass',
                   'super effective against': ['Water', 'Ground', 'Rock'],
                   'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'],
                 'not very effective against': ['Rock', 'Steel']},
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'],
               'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy',
                   'super effective against': ['Fighting', 'Dragon', 'Dark'],
                   'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug',
                     'super effective against': ['Grass', 'Psychic', 'Dark'],
                     'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy',
                      'super effective against': ['Fighting', 'Dragon', 'Dark'],
                      'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost',
                    'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']},
    'Psystrike': {'name': 'Psytrike', 'power': 100, 'type': 'Psychic',
                  'super effective against': ['Fighting', 'Poison'],
                  'not very effective against': ['Steel', 'Psychic']},
    'Aura Sphere': {'name': 'Aura Sphere', 'power': 80, 'type': 'Fighting',
                    'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
                    'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']}
}

CHARACTERS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock', 'Double Kick', 'Thunderbolt'], 'Attack': 55,
                'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': ['Crunch', 'Ember', 'Scratch', 'Wing Attack'],
                  'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle', 'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65,
                 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45,
                   'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'],
               'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience': 225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25,
                  'Moves': ['Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'], 'Attack': 35, 'Defense': 70,
                  'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49,
                  'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43,
                   'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'],
                 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': ['Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'],
              'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet', 'Ice Shard', 'Headbutt'], 'Attack': 70,
                'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'], 'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73,
              'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': ['Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28,
               'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'],
                 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61},
    'Mewtwo': {'Type': ['Psychic'], 'HP': 106, 'Moves': ['Shadow Ball', 'Psystrike', 'Aura Sphere'], 'Attack': 110,
               'Defense': 90, 'Speed': 130, 'Experience': 220}
}


# new function
def message(message):
    """Displays messages in game by creating objects"""
    # Blit and Load: https: // waylonwalker.com / pygame - image - load /
    # Fonts: https://nerdparadise.com/programming/pygame/part5
    # 10, 350, 480, 140
    pygame.draw.rect(screen, white, (10, 525, 980, 210))
    pygame.draw.rect(screen, black, (10, 525, 980, 210), 3)

    font = pygame.font.SysFont("squaresans", 30)
    text = font.render(message, True, black)

    # creates rectangle
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 625

    # connecting the text with the rectangle as one object
    screen.blit(text, text_rect)
    # updates this portion of the screen
    pygame.display.update()


# new function
def create_button(x, y, width, height, text):
    """Creates button rectangle that is highlighted when cursor hovers over it"""
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
    font = pygame.font.SysFont('squaresans', 30)
    text = font.render(f'{text}', True, black)
    text_rect = text.get_rect(center=button.center)
    screen.blit(text, text_rect)
    pygame.display.update()
    return button


class ImageButton():
    def __init__(self, x, y, image, scale, value):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.value = value

    def draw(self):
        """Draws the button on the screen"""
        # highlight border gold if cursor hovers over it
        pos = pygame.mouse.get_pos()
        cursor_hover = self.rect.collidepoint(pos)

        if cursor_hover:
            pygame.draw.rect(screen, white, self.rect)
            pygame.draw.rect(screen, gold, self.rect, 3)
        else:
            pygame.draw.rect(screen, white, self.rect)
            pygame.draw.rect(screen, white, self.rect, 3)

        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return self.value

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


def ai():
    '''Creates a trainer that chooses a random pokemon to battle you'''
    pokemonz = ['Pikachu', 'Charizard', 'Squirtle', 'Jigglypuff', 'Gengar', 'Magnemite', 'Bulbasaur', 'Charmander',
                'Beedrill', 'Golem', 'Dewgong', 'Hypno', 'Cleffa', 'Cutiefly', 'Mewtwo']
    opponent = rand.choice(pokemonz)
    return opponent


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type_ = CHARACTERS[name]['Type']
        self.HP = CHARACTERS[name]['HP']
        self.current_HP = CHARACTERS[name]['HP']
        self.Attack = CHARACTERS[name]['Attack']
        self.Defense = CHARACTERS[name]['Defense']
        self.Speed = CHARACTERS[name]['Speed']
        self.Experience_gain = CHARACTERS[name]['Experience']
        self.Moves = CHARACTERS[name]['Moves']
        self.Level = 1
        self.Experience = 0

        # set sprites position
        self.x = x
        self.y = y
        # set sprites size
        self.size = 150

        # make sprite front facing
        # self.set_sprite('front_default')

    def move_type(self, opponent, move):
        """Determines the type multiplier that effects the damage to an opposing pokemon"""
        multiplier = 1
        for type_ in opponent.type_:
            if type_ in MOVES_DICTIONARY[move]['super effective against']:
                multiplier *= 2
            if type_ in MOVES_DICTIONARY[move]['not very effective against']:
                multiplier *= (1 / 2)
        return multiplier

    def crit_chance(self):
        '''Determines if the hit is critical or not'''
        if self.Speed >= rand.randint(0, 511):
            return 2
        else:
            return 1

    def calculate_damage(self, opponent, move):
        """Calculates the amount of damage a move does to the opposing pokemon"""
        power = MOVES_DICTIONARY[move]['power']
        modifier = (rand.randrange(85, 101, 1) / 100) * self.move_type(opponent, move) * self.crit_chance()
        # https://pynative.com/python-random randrange/#:~:text=Use%20a%20random.randrange(),4%2C%206%2C%208).
        damage = (((((2 * self.Level) / 5) + 2) * power * (self.Attack / opponent.Defense)) / 50) * modifier
        return damage

    def take_damage(self, damage):
        """Deals damage to a given pokemon"""
        self.current_HP -= damage

        if self.current_HP <= 0:
            self.current_HP = 0

    # new function
    def use_attack(self, opponent, move):
        """Handles all of what happens when the user or opponent uses a move"""
        if self.move_type(opponent, move) == 2:
            message(f"{self.name} used {move} .... It was super effective!")
        elif self.move_type(opponent, move) == 0.5:
            message(f"{self.name} used {move} .... it wasn't very effective")
        else:
            message(f"{self.name} used {move}!")

        time.sleep(1.5)

        damage = self.calculate_damage(self, move)
        damage = int(damage)
        opponent.take_damage(damage)

    # new function
    def set_sprite(self, orientation):
        """Grab the image of the pixelated Pokémon from the Pokémon API"""
        # Load the image into Pygame
        self.image = pygame.image.load(f"images/{self.name}{orientation}.png")
        # https: // www.pygame.org / docs / ref / image.html  # pygame.image.load

        # scales the image
        scale = self.size / self.image.get_width() + 1.2
        nwidth = self.image.get_width() * scale
        nheight = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (nwidth, nheight))
        return self.image

    def battle_priority(self, opponent):
        '''Determines whether you or the opponent attacks first'''
        if self.Speed > opponent.Speed:
            return True
        else:
            return False

    # new function
    def move_buttons(self):
        """Creates the 3-4 move buttons for a Pokémon"""
        posx = [250, 750, 250, 750]
        posy = [94, 94, 281, 281]
        counter = 0
        move_buttons = []
        for move in self.Moves:
            button = create_button(posx[counter], posy[counter], 450, 175, str(move))  # Make 3 to 4 buttons for moves
            move_buttons.append(button)
            counter += 1
        return move_buttons

    # new function
    def paint(self, trans=255):
        """Actually puts the image in the game, as well as covering transparency"""
        sprite = self.image.copy()
        details = (255, 255, 255, trans)  # Gets image color and transparency values
        sprite.fill(details, None, pygame.BLEND_RGBA_MULT)  # None selects image, BLEND_RBGA makes image transparent
        screen.blit(sprite, (self.x, self.y))  # Blit puts image in game, position puts where in game

    # new function
    def get_rect(self):
        """Creates a rectangle object around the displayed image"""
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update_level(self, opponent):
        '''Updates the experience and level of your pokemon after a battle'''
        old_level = self.Level
        self.Experience += CHARACTERS[opponent.name]['Experience']
        self.Level = int(self.Experience ** (1 / 3))
        if self.Level > old_level:
            print('You leveled up!')
        print(f"{self.name}'s current level is: {self.Level}")

    def opp_move(self, opponent):
        '''Makes the opponent use a random move each turn'''
        return rand.choice(CHARACTERS[opponent.name]['Moves'])

    # new function
    def hp_bar(self, x, y):
        """Draws the HP bar and the text showing how much HP the Pokémon has"""
        # makes two bars and reveals the red one when the green gets smaller
        scale = 200 // self.HP
        bar = pygame.Surface((self.HP * scale, 20))
        bar.fill(red)
        current_bar = pygame.Surface((self.current_HP * scale, 20))
        current_bar.fill(green)

        # display HP text
        font = pygame.font.SysFont('squaresans', 25)
        text = font.render(f"HP: {self.current_HP} / {self.HP}", True, black)

        # makes bar pygame objects and positions them with text
        # self.bar_x and self.bar_y are defined in the game loop
        text_rect = text.get_rect(topleft=(x, y+30))
        bar_rect = bar.get_rect(topleft=(x, y))
        current_bar_rect = current_bar.get_rect(topleft=(x, y))

        # draws bars into the actual game
        screen.blit(bar, (x, y))
        screen.blit(current_bar, (x, y))
        screen.blit(text, (x, y + 30))

        # new function

    def xp_text(self, x, y):
        """Draws xp text next to the health bars"""
        # finds the max xp for the given level
        xp = 1
        for i in range(1000):
            level = self.Level + 1
            level = int(xp ** (1 / 3))
            if level > self.Level:
                break
            xp += 1

        font = pygame.font.SysFont('sqaresans', 25)
        text = font.render(f"Lvl {self.Level}: {self.Experience} / {xp}", True, black)
        text_rect = text.get_rect(topleft=(x + 120, y + 30))
        screen.blit(text, text_rect)


class Pokedex():
    def __init__(self):
        """Initializes the attributes for the Pokedex Class"""
        self.party = []

    def add_mon(self, mon):
        """Adds a pokemon to your pokedex/party"""
        self.party.append(mon)

    def mon_faint(self, mon):
        """Removes a pokemon from your pokedex/party when it faints"""
        self.party.remove(mon)

    def checklen(self):
        """Returns the length of the party"""
        return len(self.party)


def title(message, size):
    '''Title screen message given message and size of font'''
    font = pygame.font.SysFont("squaresans", size)
    text = font.render(message, True, black)

    text_rect = text.get_rect()
    text_rect.x = 50
    text_rect.y = 150
    pygame.draw.rect(screen, black, (text_rect.x - 13, text_rect.y - 13, text.get_width() + 26, text.get_height() + 26),
                     3)

    # connecting the text with the rectangle as one object
    screen.blit(text, text_rect)
    pygame.display.update()


# https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
def Background(image_file, location):
    '''Puts a background on the screen'''
    image = pygame.image.load(image_file)
    image_rect = image.get_rect()
    left, top = location
    screen.blit(image, image_rect)

# defining stuff needed for inside the while loop + some extra pokemon for your party
starter = None
trainer = None
battle_poke = None
Charizard = Pokemon("Charizard", 50, 225)
Mewtwo = Pokemon("Mewtwo", 175, 300)
Mewtwo.Level = 1000  # god mode
pokedex = Pokedex()
pokedex.add_mon(Mewtwo)
pokedex.add_mon(Charizard)
move_buttons = []
battle_choices = []
status = 'title'

# Makes Pokémon into Pokémon class object
bulbasaur = Pokemon("Bulbasaur", 50, 225)
charmander = Pokemon("Charmander", 350, 225)
squirtle = Pokemon('Squirtle', 650, 225)
starters = [bulbasaur, charmander, squirtle]

# Making buttons (Still need to change the set_sprite because Image button needs the file name not the actual image)
starter1 = ImageButton(4, 100, bulbasaur.set_sprite("front"), 1.2, "bulbasaur")
starter2 = ImageButton(335, 100, charmander.set_sprite("front"), 1.2, "charmander")
starter3 = ImageButton(666, 100, squirtle.set_sprite("front"), 1.2, "squirtle")

# used inside the game loop so that some things won't be drawn multiple times
title_drawn = False
select_drawn = False
move_drawn = False
pre_drawn = False

# Game Loop
while status != 'quit':

    # Should be at the start, quits game if red x at top of screen is hit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = 'quit'

        # If the user wants to or doesn't want to play again
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_y:
                # resets these variables so they can be drawn again
                title_drawn = False
                select_drawn = False
                move_drawn = False
                pre_drawn = False
                pokedex = None
                pokedex = Pokedex() # Resetting their party
                status = 'title'

            elif event.type == pygame.K_n:
                status = 'quit'

        # Starter selection screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_loc = event.pos
            if status == "title":
                if start_button.collidepoint(click_loc):
                    time.sleep(1)
                    title_drawn = False
                    status = "starter"

            elif status == 'starter':
                for i in range(len(starters)):
                    if starters[i].get_rect().collidepoint(click_loc):
                        starter = starters[i]

                # Need to see if a starter is selected before moving on to the next stage.
                if starter is not None:
                    starter.Level = 5
                    pokedex.add_mon(starter)
                    time.sleep(2)

                    status = 'selection'

            elif status == 'selection':
                for i in range(len(pokedex.party)):
                    # loops through each party pokemon button to see which one was clicked
                    poke_button = battle_choices[i]
                    # If click where button is, then new active pokemon
                    if poke_button.collidepoint(click_loc):
                        battle_poke = pokedex.party[i]
                        message(f"You chose {battle_poke.name}")
                        # enemy trainer
                        enemy = ai()
                        trainer = Pokemon(enemy, 250, -50)
                        time.sleep(3)
                        select_drawn = False
                        status = "pre battle"

            elif status == 'player turn':
                # loops through each button to see which one was clicked
                for i in range(len(battle_poke.Moves)-1):
                    button = move_buttons[i]
                    if button.collidepoint(click_loc):
                        move = battle_poke.Moves[i]
                        battle_poke.use_attack(trainer, move)
                        time.sleep(2)
                        move_drawn = False
                    if trainer.current_HP == 0:
                        status = 'trainer faint'
                    else:
                        status = 'trainer turn'
    if status == "title":
        # draw once to prevent flickering
        while not title_drawn:
            screen.fill(white)
            Background('images/gen_background.png', [0, 0])
            title('Welcome to the Wonderful World of Pokemon', 60)
            pygame.draw.rect(screen, black, (447, 372, 106, 106), 3)
            title_drawn = True
        start_button = create_button(450, 375, 100, 100, "Start")
        #pygame.display.update()

    elif status == 'starter':
        screen.fill(white)
        Background('images/gen_background.png', [0, 0])
        starter1.draw()  # Drawing the buttons on the screen
        starter2.draw()
        starter3.draw()
        # black outline around each pokemon using ImageButton class __init__ defintiion
        width = starter1.width
        height = starter1.height
        pygame.draw.rect(screen, black, (1, 97, width + 6, height + 6), 3)
        pygame.draw.rect(screen, black, (332, 97, width + 6, height + 6), 3)
        pygame.draw.rect(screen, black, (663, 97, width + 6, height + 6), 3)
        message("Choose your starter Pokémon!")

        #pygame.display.update()

    elif status == 'selection':
        x = [15, 340, 665, 15, 340, 665]
        y = [535, 535, 535, 635, 635, 635]
        # draw once to prevent flickering
        while not select_drawn:
            screen.fill(white)
            Background('images/battle_background.png', [0, 0])
            title('A trainer has appeared ... choose your Pokémon!', 55)
            message('')
            select_drawn = True
        #Reset battle choices list so the buttons are reset before being made again
        battle_choices = []
        # select Pokémon buttons appear
        for i in range(len(pokedex.party)):
            # Creating buttons for each pokemon in the party
            button = create_button(x[i], y[i], 320, 95, pokedex.party[i].name)
            # black outline of each button
            battle_choices.append(button)

    elif status == 'pre battle':
        screen.fill(white)
        Background('images/battle_background.png', [0, 0])
        #pygame.display.update()

        # trainer repositioning and fading in
        trainer.x = 520
        trainer.y = 20
        trainer.size = 300
        trainer.set_sprite('front')

        # # makes Pokémon fade in using the trans feature in paint (doesn't work)
        # transparency = 0
        # while transparency < 255:
        #     screen.fill(white)
        #     Background('images/battle_background.png', [0, 0])
        #     trainer.paint(transparency)
        #     transparency += 1
        #     message(f"Trainer sent out {trainer.name}!")
        #     # update screen so trainer Pokémon will appear before player Pokémon
        #     pygame.display.update()
        #
        # time.sleep(2)
        trainer.paint()
        message(f"Trainer sent out {trainer.name}!")
        time.sleep(2)

        # player repositioning and fade
        battle_poke.x = 0
        battle_poke.y = 160
        battle_poke.size = 300
        battle_poke.set_sprite('back')

        # doesn't work
        # transparency = 0
        # while transparency < 255:
        #     screen.fill(white)
        #     Background('images/battle_background.png', [0, 0])
        #     trainer.paint()
        #     battle_poke.paint(transparency)
        #     transparency += 1
        #     message(f"You sent out {battle_poke.name}!")
        battle_poke.paint()
        message(f"You sent out {battle_poke.name}!")
        time.sleep(2)


        # drawing the hp and xp of the player and trainer
        battle_poke.hp_bar(420, 400)
        trainer.hp_bar(700, 175)
        battle_poke.xp_text(420, 400)
        trainer.xp_text(500, 175)

        priority = battle_poke.battle_priority(trainer)
        if priority:
            status = 'player turn'
        else:
            status = 'trainer turn'

        #pygame.display.update()

    if status == 'player turn':
        posx = [50, 510, 50, 510]
        posy = [530, 530, 635, 635]
        # draw once to prevent flickering
        if not move_drawn:
            screen.fill(white)
            Background('images/battle_background.png', [0, 0])
            battle_poke.paint()
            trainer.paint()
            message('')

        battle_poke.hp_bar(400, 400)
        trainer.hp_bar(200, 100)
        battle_poke.xp_text(400, 400)
        trainer.xp_text(200, 100)
        #pygame.display.update()

        # creating the move buttons
        for i in range(len(battle_poke.Moves)):
            try:
                button = create_button(posx[i], posy[i], 450, 100, battle_poke.Moves[i])  # Make 3 to 4 buttons for moves
            except:
                continue
            # black outline of buttons
            # pygame.draw.rect(screen, black, (posx[i], posy[i], 450, 100), 3)
            move_buttons.append(button)
        time.sleep(3)

    if status == 'trainer turn':
        screen.fill(white)
        Background('images/battle_background.png', [0, 0])
        battle_poke.paint()
        trainer.paint()
        battle_poke.hp_bar(500, 400)
        trainer.hp_bar(100, 100)
        battle_poke.xp_text(500, 400)
        trainer.xp_text(100, 100)
        #pygame.display.update()

        # buffer zone between player and trainer turns
        message('')
        time.sleep(2)

        message(f'Trainer turn: What will {trainer.name} do?')
        time.sleep(3)

        message('.....')
        time.sleep(2)

        move = battle_poke.opp_move(trainer)
        trainer.use_attack(battle_poke, move)
        time.sleep(2)

        if battle_poke.current_HP == 0:
            status = 'player faint'
        else:
            status = 'player turn'

        #pygame.display.update()

    # this should be correct, but I'm unsure about the status loop(to pre battle)
    if status == 'player faint':
        # make Pokémon slowly fade out
        trans = 255
        while trans > 0:
            screen.fill(white)
            Background('images/battle_background.png', [0, 0])
            battle_poke.hp_bar(400, 400)
            trainer.hp_bar(200, 100)
            battle_poke.xp_text(400, 400)
            trainer.xp_text(200, 100)
            battle_poke.paint(trans)
            trainer.paint()

            message(f"{battle_poke.name} fainted!")
            trans -= 1

        # removes Pokémon from Pokédex and if you still have another Pokémon loops back, so you can fight with it
        pokedex.mon_faint(battle_poke)
        battle_poke = None
        if pokedex.checklen() == 0:
            status = 'game over'
        else:
            status = 'selection'
        #pygame.display.update()

    if status == 'trainer faint':
        # make Pokémon slowly fade out
        trans = 255
        while trans > 0:
            screen.fill(white)
            Background('images/battle_background.png', [0, 0])
            battle_poke.hp_bar(400, 400)
            trainer.hp_bar(200, 100)
            battle_poke.xp_text(400, 400)
            trainer.xp_text(200, 100)
            battle_poke.paint()
            trainer.paint(trans)
            message(f"{trainer.name} fainted!")
            trans = trans - 50
            time.sleep(0.5)
        # resetting the health of each Pokémon
        battle_poke.current_HP = battle_poke.HP
        trainer.current_HP = trainer.HP
        battle_poke.update_level(trainer)
        if len(pokedex.party) < 6: #Checking if the player already has six pokemon.
            pokedex.add_mon(trainer) #Add if they dont
            print(pokedex.party)
        trainer = None #Reseting to make sure the old pokemon isnt attached to the ai

        # resets these variables so the screens can be drawn again
        title_drawn = False
        select_drawn = False
        move_drawn = False
        pre_drawn = False
        status = 'selection'
        #pygame.display.update()

    if status == 'game over':
        message(f"You lost, you are not cut out to be a pokemon master")
        time.sleep(5)
        message(f"Do you want to play again?(Y/N)")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

# Notes at the bottom for Andrew
#
#     - Made it so if opponent faints then their pokemon is added to party, and also if their pokemon faints while battling someone else, they just find a new opponent instead, rather than choosing another pokemon to continue fighting the same opponent.
#     -It should loop through the game and if they press y at any point, it should take them to the title screen and clear their party
#     -Theres an issue where in the selection screen if someone has more than three pokemon, the ones after cannot be selected. (The buttons appear but they cant be clicked on), I didn't want to try and mess things up so just take a look at the selection function when you get the chance.'
#     -Also all of this is still pretty buggy for me but I think theres a good chance it might just be my computer. Things should work but I don't know for sure, because every time I launch the game I have the lovely spinny wheel thingy'
#     -May have left things out, let me know if theres anything u dont understand or recognize, and it may have been my doing.
#     -As it is now, it doesn't look like i'll be in class for coding tomorrow but we'll see' If not, I can try to be awake by coding class and be somewhat useful
#     -Text me if u have any other questions