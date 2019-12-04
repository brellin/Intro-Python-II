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


# Write a loop that:
has_quit = False

user_room = user.current_room

while not has_quit:

    # * Prints the current room name and prints the current description (the textwrap module might be useful here)
    print(f"\n{user_room.name}: {user_room.description}\n")

    # * Waits for user input and decides what to do.
    which_dir = input('''Which direction would you like to go?
Type N, S, E, or W: ''')
    which_dir = which_dir.upper()

    # If the user enters "q", quit the game.
    if (which_dir == 'Q'):
        has_quit = True
        print(f'\n\nSad to see you go, {user.name} T_T')

    # If the user enters a cardinal direction, attempt to move to the room there.
    if (which_dir == 'N' and not user_room.n_to == None):
        user_room = user_room.n_to
    elif (which_dir == 'S' and not user_room.s_to == None):
        user_room = user_room.s_to
    elif (which_dir == 'E' and not user_room.e_to == None):
        user_room = user_room.e_to
    elif (which_dir == 'W' and not user_room.w_to == None):
        user_room = user_room.w_to
        # Prints an error message if the movement isn't allowed.
    else:
        print('Sadly, you cannot move this direction.')
