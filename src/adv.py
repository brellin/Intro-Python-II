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

item_list = {
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
room['outside'].add_item_to_room(item_list['arrows'])
room['foyer'].add_item_to_room(item_list['sword'])
room['overlook'].add_item_to_room(item_list['bow'])
room['treasure'].add_item_to_room(item_list['jewel'])
room['treasure'].add_item_to_room(item_list['ring'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player(input('Choose your name: '), room['outside'])

has_quit = False

welcome_help_text = f'''\nWelcome to my game, {user.name}!
It's a simple, text-based game, 
but you do have a few options as to what you can do. 
You can:
\tType the first letter of a cardinal direction to attempt to move in that direction,
\t"GET"/"TAKE" and the name of an item in the current room,
\t"I"/"INVENTORY" to view the items in your inventory,
\t"DROP" and the name of an item in your inventory,
\t"H"/"HELP" to view this screen again,
\tor "Q"/"QUIT" to quit.\n\n'''

print(welcome_help_text)

# Write a loop that:
while not has_quit:

    current_room = user.current_room

    # * Prints the current room name and prints the current description (the textwrap module might be useful here)
    print(f"\n{current_room.name}: {current_room.description}\n")
    if (current_room.has_items()):
        print(f'Item(s) in {current_room.name}:')
        for item in current_room.item_list:
            print(f'\t{item.name}: {item.description}')
        print('\n')

    # * Waits for user input and decides what to do.
    user_input = input('What would you like to do? ').upper()

    split_input = user_input.split(' ')

    room_dirs = {
        'N': current_room.n_to,
        'S': current_room.s_to,
        'E': current_room.e_to,
        'W': current_room.w_to
    }

    dir_names = {
        'N': 'North',
        'S': 'South',
        'E': 'East',
        'W': 'West'
    }

    # If the user enters "q", quit the game.
    if (user_input == 'Q' or user_input == 'QUIT'):
        has_quit = True
        print(f'\nSad to see you go, {user.name} T_T')

    # If action and object words
    elif (len(split_input) > 1):

        # Declare word variables
        action_word = split_input[0]
        input_item = split_input[1]
        item_list_item = item_list.get(input_item.lower())

        # If action word is get or take and current room has the item
        if ((action_word == 'GET' or action_word == 'TAKE') and current_room.has_item(item_list_item)):

            # Remove item from current room
            current_room.remove_item_from_room(item_list_item)

            # Add item to user's inventory
            user.add_item_to_inventory(item_list_item)

            # Invoke item's method for taking
            item_list_item.on_take()

        # If action word is drop and item is in user's inventory
        elif (action_word == 'DROP' and user.has_item(item_list_item)):

            # Remove item from user's inventory
            user.drop_item(item_list_item)

            # Add item to current room
            current_room.add_item_to_room(item_list_item)

            # Invoke item's method for dropping
            item_list_item.on_drop()

        else:

            if (not (action_word == 'GET' or action_word == 'TAKE' or action_word == 'DROP')):
                print(
                    f'"{action_word}" is not a recognized command.\nType "H" or "HELP" for help.')

            else:
                print(
                    f'Sorry, "{input_item}" is not in {current_room}.\nPlease check your spelling and try again.')

    elif (user_input == 'I' or user_input == 'INVENTORY'):

        if(len(user.inventory) > 0):
            print(f'\n{user.name}\'s Inventory:')
            for inventory_item in user.inventory:
                print(f'\t{inventory_item.name}: {inventory_item.description}')

        else:
            print(
                '\nYou have no items in your inventory.\n\nTry roaming around to find some items.')

    elif (user_input == 'H' or user_input == 'HELP'):
        print(welcome_help_text)

    # If the user enters a cardinal direction, attempt to move to the room there.
    elif ((user_input == 'N' or user_input == 'S' or user_input == 'E' or user_input == 'W') and not room_dirs[user_input] == None):
        user.move(room_dirs[user_input])

    # Prints an error message if the movement isn't allowed.
    elif(user_input == 'N' or user_input == 'S' or user_input == 'E' or user_input == 'W'):
        direction = dir_names[user_input]
        print(f'Sadly, you cannot move {direction} from this location.')

    else:
        print(
            f'"{user_input}" is not a recognized command.\nType "H" or "HELP" for help.')
