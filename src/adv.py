import random
from room import Room
from player import Player
from item import Item, Potion, Weapon, Quest_Item
from monster import Monster

# Declare all the rooms

room = {

    'outside':  Room('Outside Cave Entrance', 'North of you, the cave mount beckons'),

    'foyer':    Room('Foyer',
                     '''Dim light filters in from the south. Dusty
passages run north and east.'''),

    'overlook': Room('Grand Overlook',
                     '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance. Above you, you see a platform with a bridge
that leads toward the light.'''),

    'narrow':   Room('Narrow Passage',
                     '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),

    'treasure': Room('Treasure Chamber', f'''You've found the long-lost treasure
chamber! The only exit is to the south.'''),

    'staircase': Room('Staircase',
                      '''Stairs connecting the downstairs to the upstairs 
of this house.Nothing interesting, just some stone stairs.
Move north to go upstairs and south to go downstairs.'''),

    'loft': Room('Loft',
                 '''The staircase opens to a quaint room with a rail, 
overlooking the foyer to the south. There is a comfy 
looking chair and a nightstand sitting next to the rail.
Does somebody live here???
To the north, there is a nifty door that leads to - what looks like - a balcony.'''),

    'balcony': Room('Balcony',
                    '''Stepping out the door and onto the balcony, you see 
that there is a rickety, wooden bridge that leads
toward a light shining in the distance, but 
you can\'t make out what the light is from here. '''),

    'bridge': Room('Bridge',
                   '''Underneath you is an unstable bridge with ragged ropes
keeping it from falling into the massive chasm beneath you.'''),

    'light': Room('Light Source',
                  '''You have reached the source of the flickering light that 
you could see from across the chasm you just crossed.
You can see that the light originated from a pedastal 
that now stands in front of you. This pedastal has a
slot that looks like a jewel can fit inside...''')

}

item_list = {
    'jewel': Quest_Item('Jewel', 'A jewel that looks like it could have belonged to royalty at one time.', room['light']),
    'ring': Item('Ring', 'A simple ring.'),
    'sword': Weapon('Sword', 'Your average, everyday, run-of-the-mill sword.', 1),
    'bow': Item('Bow', 'Just a bow. No arrows...'),
    'arrows': Item('Arrows', 'A bundle of arrows, no bow...'),
    'potion': Potion('Potion', 'Heals you for 5 health points.', 5),
}

monsters = {
    'ogre': Monster('Ogre'),
    'ogre2': Monster('Ogre'),
    'goblin': Monster('Goblin', None, 3, 1),
    'goblin2': Monster('Goblin', None, 3, 1),
    'goblin3': Monster('Goblin', None, 3, 1),
    'boss': Monster('Big Boss', None, 10, 2),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['staircase']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['staircase'].s_to = room['foyer']
room['staircase'].n_to = room['loft']
room['loft'].w_to = room['staircase']
room['loft'].n_to = room['balcony']
room['balcony'].s_to = room['loft']
room['balcony'].n_to = room['bridge']
room['bridge'].s_to = room['balcony']
room['bridge'].n_to = room['light']
room['light'].s_to = room['bridge']

# Add items to rooms
room['outside'].add_item_to_room(item_list['arrows'])
room['foyer'].add_item_to_room(item_list['sword'])
room['foyer'].add_item_to_room(item_list['potion'])
room['overlook'].add_item_to_room(item_list['bow'])
room['treasure'].add_item_to_room(item_list['jewel'])
room['treasure'].add_item_to_room(item_list['ring'])
room['treasure'].add_item_to_room(item_list['potion'])
room['loft'].add_item_to_room(item_list['potion'])
room['balcony'].add_item_to_room(item_list['potion'])
room['bridge'].add_item_to_room(item_list['potion'])

# Add monsters to rooms
room['foyer'].add_monster_to_room(monsters['ogre'])
room['narrow'].add_monster_to_room(monsters['ogre2'])
room['bridge'].add_monster_to_room(monsters['goblin'])
room['bridge'].add_monster_to_room(monsters['goblin2'])
room['bridge'].add_monster_to_room(monsters['goblin3'])
room['light'].add_monster_to_room(monsters['boss'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player(input('Choose your name: '), room['outside'])

global crashed
crashed = False

welcome_help_text = f'''\nWelcome to my game, {user.name}!
It's a simple, text-based game, 
but you do have a few options as to what you can do. 
You can:
\tType the first letter of a cardinal direction to attempt to move in that direction,
\t"GET" or "TAKE" and the name of an item in the current room,
\t"I" or "INVENTORY" to view the items in your inventory,
\t"DROP" and the name of an item in your inventory,
\t"F" or "FIGHT" and the name of a monster to enter battle with the monster,
\t"HP" or "HEALTH" to view your health,
\t"U" or "USE" to use an item,
\t"H" or "HELP" to view this screen again,
\tor "Q" or "QUIT" to quit the game.\n\n'''


def print_help():
    print(welcome_help_text)


print_help()

# Write a loop that:
while not crashed:

    current_room = user.current_room

    # * Prints the current room name and prints the current description (the textwrap module might be useful here)
    if (current_room == room['light'] and current_room.has_monsters()):
        fight_monster(current_room.monster_list[0])

    print(f"\n{current_room.name}: {current_room.description}\n")

    current_room.print_contents()

    # * Waits for user input and decides what to do.
    command = input('\nWhat would you like to do? ').upper()

    split_input = command.split(' ')

    room_dirs = {
        'N': {
            'check': current_room.n_to,
            'name': 'North'
        },
        'S': {
            'check': current_room.s_to,
            'name': 'South'
        },
        'E': {
            'check': current_room.e_to,
            'name': 'East'
        },
        'W': {
            'check': current_room.w_to,
            'name': 'West'
        },
    }

    def pick_up_item(selection):
        if(current_room.has_item(selection)):
            current_room.remove_item_from_room(selection)
            user.add_item_to_inventory(selection)
        else:
            print(
                f'"{selection}" is not in {current_room}.\nPlease check your spelling and try again.')

    def drop_item(selection):
        if(user.has_item(selection)):
            user.drop_item(selection)
            current_room.add_item_to_room(selection)
        else:
            print(
                f'"{selection}" is not in your inventory.\nPlease check your spelling and try again.')

    def move_to_room():
        if (current_room.has_monsters()):
            fight_monster(current_room.monster_list[0])
        elif (room_dirs[command]['check'] == None):
            # Prints an error message if the movement isn't allowed.
            direction = room_dirs[command]['name']
            print(
                f'Sadly, you cannot move {direction} from this location.')
        else:
            # If the user enters a cardinal direction, attempt to move to the room there.
            user.move(room_dirs[command]['check'])

    def quit_game():
        global crashed
        crashed = True
        print(f'\nUntil next time, {user.name}!')

    def unrecognized(bad):
        print(
            f'"{bad}" is not a recognized command.\nType "H" or "HELP" for help.')

    def fight_monster(monster):
        if (current_room.has_monster(monster)):
            combat = True
            while combat:

                commands = {
                    'B': user.block,
                    'BLOCK': user.block,
                    'A': user.attack,
                    'ATTACK': user.attack,
                }

                command = input(
                    f'\nAttack {monster.name} - or block {monster.name}\'s attack! ').upper()

                if (command in commands.keys()):
                    commands[command](monster, current_room)

                    randomizer = random.randint(0, 10)

                    monster.attack(
                        user, current_room) if randomizer > 3 else monster.block(user, current_room)
                else:
                    unrecognized(command)

                if (monster.hp <= 0 or user.hp <= 0):
                    if (user.hp <= 0):
                        crashed = True
                    combat = False

    commands = {
        'GET': pick_up_item,
        'TAKE': pick_up_item,
        'DROP': drop_item,
        'N': move_to_room,
        'S': move_to_room,
        'E': move_to_room,
        'W': move_to_room,
        'Q': quit_game,
        'QUIT': quit_game,
        'I': user.print_inventory,
        'INVENTORY': user.print_inventory,
        'H': print_help,
        'HELP': print_help,
        'F': fight_monster,
        'FIGHT': fight_monster,
        'HP': user.print_health,
        'HEALTH': user.print_health,
        'U': user.use_item,
        'USE': user.use_item,
        'EQUIP': user.use_item,
    }

    if (len(split_input) > 1):

        verb = split_input[0]
        obj = split_input[1]

        if (verb in commands.keys()):

            if (not (verb == 'F' or verb == 'FIGHT')):
                item_list_item = item_list.get(obj.lower())
                commands[verb](item_list_item)

            else:
                monster_list_monster = monsters.get(obj.lower())
                commands[verb](monster_list_monster)

        else:
            unrecognized(verb)

    elif (command in commands.keys()):
        commands[command]()

    else:
        unrecognized(command)
