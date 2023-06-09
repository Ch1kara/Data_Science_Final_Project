# Initial Base Code for Word Game
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
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']},
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']},
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']},
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']},
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']},
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']},
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']},
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']},
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']},
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']},
    'Psystrike' : {'name' : 'Psytrike', 'power': 100, 'type':'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Steel', 'Psychic']},
    'Aura Sphere': {'name': 'Aura Sphere', 'power':80, 'type': 'Fighting', 'super effective against': ['Normal','Ice','Rock','Dark','Steel'], 'not very effective against': ['Poison','Flying','Psychic','Bug','Fairy']}
}


CHARACTERS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience':225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61},
    'Mewtwo': {'Type': ['Psychic'], 'HP': 106, 'Moves': ['Shadow Ball', 'Psystrike', 'Aura Sphere'], 'Attack': 110, 'Defense': 90, 'Speed':130, 'Experience':220}
}

# Create your Classes here

import random as rand

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.type_ = CHARACTERS[name]['Type']
        self.HP = CHARACTERS[name]['HP']
        self.Attack = CHARACTERS[name]['Attack']
        self.Defense = CHARACTERS[name]['Defense']
        self.Speed = CHARACTERS[name]['Speed']
        self.Experience_gain = CHARACTERS[name]['Experience']
        self.Moves = CHARACTERS[name]['Moves']
        self.Level = 1
        self.Experience = 0


    def __repr__(self):
        """How a pokemon is displayed when called on"""
        return f"{self.name}|Level:{self.Level}|XP:{self.Experience}"


    def battle_priority(self, opponent):
        '''Determines whether you or the opponent attacks first'''
        if self.Speed > opponent.Speed:
            return True
        else:
            return False


    def choose_move(self):
        '''Allows you to choose a move from the user pokemon's moveset'''
        print(f'Here are the moves:')
        counter = 1
        for move in self.Moves:
            print(f'{move} ({counter})')
            counter += 1
        select = int(input('Choose your move(number): '))
        return MOVES_DICTIONARY[self.Moves[select-1]]['name']


    def move_type(self,opponent,move):
        """Determines the type multiplier that effects the damage to an opposing pokemon"""
        multiplier = 1
        for type_ in opponent.type_:
            if type_ in MOVES_DICTIONARY[move]['super effective against']:
                multiplier *= 2
            if type_ in MOVES_DICTIONARY[move]['not very effective against']:
                multiplier *= (1/2)
        return multiplier


    def crit_chance(self):
        '''Determines if the hit is critical or not'''
        if self.Speed >= rand.randint(0,511):
            print("Critical Hit!")
            return 2
        else:
            return 1


    def calculate_damage(self, opponent, move):
        """Calculates the amount of damage a move does to the opposing pokemon"""
        power = MOVES_DICTIONARY[move]['power']
        modifier = (rand.randrange(85,101,1)/100)*self.move_type(opponent,move)*self.crit_chance()
        #https://pynative.com/python-random randrange/#:~:text=Use%20a%20random.randrange(),4%2C%206%2C%208).
        damage = (((((2*self.Level)/5)+2)*power*(self.Attack/opponent.Defense))/50)*modifier
        return damage


    def update_level(self,opponent):
        '''Updates the experience and level of your pokemon after a battle'''
        old_level = self.Level
        self.Experience += CHARACTERS[opponent.name]['Experience']
        self.Level = int(self.Experience**(1/3))
        if self.Level > old_level:
            print('You leveled up!')
        print(f"{self.name}'s current level is: {self.Level}")


    def opp_move(self, opponent):
        '''Makes the opponent use a random move each turn'''
        return rand.choice(CHARACTERS[opponent.name]['Moves'])


    def battle(self,opponent):
        '''Runs the fight between two pokemon'''
        print(f"A trainer appears ... {opponent.name} wants to fight!")
        #add the "run" away possibility here, at least I'm pretty sure this is where you'll add it
        run = input("Would you like to run? Yes or no?")
        if run == "yes":
            print("You cannot run from a trainer battle ....\n––––––––––")
        priority = self.battle_priority(opponent)
        print(f"Your {self.name}'s health: {self.HP}HP")
        print(f"Opponent's {opponent.name}'s health: {opponent.HP}HP\n")
        print('––––––––––')
        while self.HP > 0 and opponent.HP > 0:
            if priority: #if the player moves first
                print('Your turn:')
                print(f"What will {self.name} do?\n")
                move = self.choose_move()
                dmg = self.calculate_damage(opponent,move)
                opponent.HP -= dmg
                if self.move_type(opponent,move) == 2: #Changes based on whether the move was super effective, effective, or not very effective
                    print(f'{self.name} used {move} .... It was super effective! Your Pokemon dealt {dmg:.2f} to {opponent.name}')
                    print(f'Your {self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                elif self.move_type(opponent,move) == 0.5:
                    print(f"{self.name} used {move} .... it wasn't very effective. Your Pokemon dealt {dmg:.2f} to {opponent.name}")
                    print(f'Your {self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                else:
                    print(f"{self.name} used {move}. Your Pokemon dealt {dmg:.2f} to {opponent.name}")
                    print(f'Your {self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                priority = False
            elif priority == False:
                print("Opponent's turn:")
                print(f"What will {opponent.name} do?\n")
                move = opponent.opp_move(opponent)
                dmg = opponent.calculate_damage(self,move)
                self.HP -= dmg
                if opponent.move_type(self,move) == 2: #Changes based on whether the move was super effective, effective, or not very effective
                    print(f"{opponent.name} used {move} .... It was super effective! Your opponent's Pokemon dealt {dmg:.2f} to {self.name}")
                    print(f'Your {self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                elif opponent.move_type(self,move) == 0.5:
                    print(f"{opponent.name} used {move} .... it wasn't very effective. Your opponent's Pokemon dealt {dmg:.2f} to {self.name}")
                    print(f'{self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                else:
                    print(f"{opponent.name} used {move}. Your opponent's Pokemon dealt {dmg:.2f} to {self.name}")
                    print(f'Your {self.name}: {self.HP:.2f}HP')
                    print(f"Opponent's {opponent.name}: {opponent.HP:.2f}HP")
                    print('––––––––––')
                priority = True
        if self.HP <= 0:
            self.HP = 0
            print(f"{self.name} fainted!")
            return "Loss"

        if opponent.HP <= 0:
            opponent.HP = 0
            print(f"{opponent.name} fainted!")
            self.update_level(opponent)
            return "Win"


class Pokedex:
    def __init__(self):
        """Initializes the attributes for the Pokedex Class"""
        self.party = []


    def add_mon(self,mon):
        """Adds a pokemon to your pokedex/party"""
        self.party.append(mon)


    def mon_faint(self,mon):
        """Removes a pokemon from your pokedex/party when it faints"""
        self.party.remove(mon)


    def choose_fighter(self):
        """Choose which one of your pokemon you want to fight with"""
        print(f"Your current party: {self.party}")
        fighter = int(input("Choose your Pokemon for the next battle!(number): "))
        choice = self.party[fighter-1]
        print(f"You chose {choice}!")
        return choice


    def checklen(self):
        """Returns the length of the party"""
        return len(self.party)


    def __str__(self):
        """Returns your party"""
        string = ""
        counter = 1
        for poke in self.party:
            string += (f"{poke.__repr__()}({counter})")
            counter += 1
        return string


def ai():
    '''Creates a trainer that chooses a random pokemon to battle you'''
    pokemonz =['Pikachu','Charizard','Squirtle','Jigglypuff','Gengar','Magnemite','Bulbasaur','Charmander','Beedrill','Golem','Dewgong','Hypno','Cleffa','Cutiefly','Mewtwo']
    opponent = rand.choice(pokemonz)
    return opponent

def main():
    """Code that uses the above classes and functions to create a working game program"""
    enemy = ai()
    trainer = Pokemon(enemy)
    p = Pokedex()
    splash = print(r"""Welcome to a simplified Python version of:
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")
    start = input("Choose your starter Pokemon: Bulbasaur(1), Charmander(2), or Squirtle(3)?")
    if start == '1':
        poke = "Bulbasaur"
    elif start == '2':
        poke = 'Charmander'
    elif start == '3':
        poke = 'Squirtle'
    starter = Pokemon(poke)
    starter.Level = 5
    p.add_mon(starter)
    print(f"You have chosen {starter} as your starter Pokemon!\n––––––––––")
    T_HP = trainer.HP
    S_HP = starter.HP
    battle1 = starter.battle(trainer)
    if battle1 == "Loss":
        print("You lost, you are not cut out to be a pokemon master.")
        p.mon_faint(starter)
    elif battle1 == "Win":
        trainer.HP = T_HP
        starter.HP = S_HP
        p.add_mon(trainer)
    while p.checklen() > 0:
        enemy = ai()
        trainer = Pokemon(enemy)
        T_HP = trainer.HP
        poke_name = p.choose_fighter()
        P_HP= poke_name.HP
        battle = poke_name.battle(trainer)
        if battle == "Loss":
            p.mon_faint(poke_name)
            print(p)
            if p.checklen() == 0:
                print("You lost on your way to becoming a pokemon master. Hopefully you are more fortunate in your future travels.")
                break
            else:
                print("They got away.")
        elif battle == "Win":
            p.add_mon(trainer)
            trainer.HP = T_HP
            poke_name.HP = P_HP

#runs the program
if __name__ == "__main__":
    main()

