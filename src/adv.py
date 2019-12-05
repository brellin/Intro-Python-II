from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'jewel': Item('Jewel', 'A jewel that looks like it could have belonged to royalty at one time.'),
    'ring': Item('Ring', 'A simple ring.'),
    'sword': Item('Sword', 'Your average, everyday, run-of-the-mill sword.'),
    'bow': Item('Bow', 'Just a bow. No arrows...'),
    'arrows': Item('Arrows', 'A bundle of arrows, no bow...')
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['outside'].add_item_to_room(item['arrows'])
room['foyer'].add_item_to_room(item['sword'])
room['overlook'].add_item_to_room(item['bow'])
room['treasure'].add_item_to_room(item['jewel'])
room['treasure'].add_item_to_room(item['ring'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player(input('Choose your name: '), room['outside'])

has_quit = False


# Write a loop that:
while not has_quit:

    user_room = user.current_room

    # * Prints the current room name and prints the current description (the textwrap module might be useful here)
    print(f"\n{user_room.name}: {user_room.description}\n")
    if (len(user_room.item_list) > 0):
        print(f'Item(s) in {user_room.name}:')
        for item in user_room.item_list:
            print(f'\t{item.name}: {item.description}')
        print('\n')

    # * Waits for user input and decides what to do.
    which_dir = input(
        'Which direction would you like to go?\n\nType "N", "S", "E", or "W" ("Q" to quit): ').upper()

    room_dirs = {
        'N': user_room.n_to,
        'S': user_room.s_to,
        'E': user_room.e_to,
        'W': user_room.w_to
    }

    dir_names = {
        'N': 'North',
        'S': 'South',
        'E': 'East',
        'W': 'West'
    }

    # If the user enters "q", quit the game.
    if (which_dir == 'Q'):
        has_quit = True
        print(f'\nSad to see you go, {user.name} T_T')

    elif(not which_dir == ('N' or 'S' or 'E' or 'W' or 'Q')):
        print(
            f'Sorry, "{which_dir}" is not a recognized input. Please try again.')
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif (not room_dirs[which_dir] == None):
        user.move(room_dirs[which_dir])

    # Prints an error message if the movement isn't allowed.
    else:
        direction = dir_names[which_dir]
        print(f'Sadly, you cannot move {direction} from this location.')
