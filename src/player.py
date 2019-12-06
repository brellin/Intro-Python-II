from item import Potion


class Player():

    def __init__(self, name, current_room, dmg=2, hp=10):
        self.name = name
        self.current_room = current_room
        self.dmg = dmg
        self.hp = hp
        self.max_hp = hp
        self.inventory = list()
        self.blocking = False

    def __str__(self):
        return f'Player(name: {self.name}, current_room: {self.current_room})'

    def move(self, room):
        self.current_room = room

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        item.on_take()

    def drop_item(self, item):
        self.inventory.remove(item)
        item.on_drop()

    def use_item(self, item):
        if (type(item) == Potion):
            item.amount = item.amount if self.hp + \
                item.amount <= self.max_hp else self.max_hp - self.hp
            self.inventory.remove(item)
            item.on_use()
            self.hp += item.amount
            print(f'\nYou now have {self.hp} health.')
        else:
            print(f'\nYou cannot use {item.name}.')

    def has_item(self, item):
        return item in self.inventory

    def print_inventory(self):
        if(len(self.inventory) > 0):
            print(f'\n{self.name}\'s Inventory:')
            for inventory_item in self.inventory:
                print(f'\t{inventory_item.name}: {inventory_item.description}')
        else:
            print(
                '\nYou have no items in your inventory.\n\nTry roaming around to find some items.')

    def print_health(self):
        print(f'You currently have {self.hp} health.')

    def take_damage(self, attacker):

        if (not self.blocking):
            self.hp -= attacker.dmg

            if (self.hp <= 0):
                print('\nYou have died. Play again!')

            else:
                print(
                    f'\nYou took {attacker.dmg} damage and you now have {self.hp} hit points remaining.')

        else:
            self.blocking = False
            print(f'\nYou blocked {attacker.name}\'s attack!')

    def attack(self, obj):
        obj.take_damage(self)

    def block(self, obj):
        self.blocking = True
