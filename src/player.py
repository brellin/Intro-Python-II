# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = list()

    def __str__(self):
        return f'Player(name: {self.name}, current_room: {self.current_room})'

    def move(self, room):
        self.current_room = room

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def has_item(self, item):
        return item in self.inventory
