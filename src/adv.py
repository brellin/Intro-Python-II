from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player(input('Choose your name: '), room['outside'])

has_quit = False

user_room = user.current_room

# Write a loop that:
while not has_quit:

    # * Prints the current room name and prints the current description (the textwrap module might be useful here)
    print(f"\n{user_room.name}: {user_room.description}\n")
    if (len(user_room.item_list) > 0):
        print(f'Item(s) in {user_room.name}')
        for item in user_room.item_list:
            print(f'{item.name}: {item.description}')

    # * Waits for user input and decides what to do.
    which_dir = input('''Which direction would you like to go?
Type "N", "S", "E", or "W" ("Q" to quit): ''')
    which_dir = which_dir.upper()

    # If the user enters a cardinal direction, attempt to move to the room there.
    if (which_dir == 'N' and not user_room.n_to == None):
        user_room = user_room.n_to
    elif (which_dir == 'S' and not user_room.s_to == None):
        user_room = user_room.s_to
    elif (which_dir == 'E' and not user_room.e_to == None):
        user_room = user_room.e_to
    elif (which_dir == 'W' and not user_room.w_to == None):
        user_room = user_room.w_to
    # If the user enters "q", quit the game and print an error message if the movement isn't allowed.
    elif (which_dir == 'Q'):
        has_quit = True
        print(f'\nSad to see you go, {user.name} T_T')
    else:

        def get_dir_name(curr):
            dirs = {
                'N': 'North',
                'S': 'South',
                'E': 'East',
                'W': 'West'
            }
            return dirs.get(curr)
        direction = get_dir_name(which_dir)
        print(f'Sadly, you cannot move {direction} from this location.')
