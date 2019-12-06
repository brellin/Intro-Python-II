from item import Potion, Weapon, Quest_Item


class Player():

    def __init__(self, name, current_room, dmg=2, hp=10):
        self.name = name
        self.current_room = current_room
        self.dmg = dmg
        self.hp = hp
        self.max_hp = hp
        self.inventory = list()
        self.blocking = False
        self.equipped = None

    def __str__(self):
        return f'Player(name: {self.name}, current_room: {self.current_room})'

    def move(self, room):
        self.current_room = room

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        item.on_take()

    def drop_item(self, item):
        self.inventory.remove(item) if item.droppable == True else None
        item.on_drop()

    def use_item(self, item):
        if (type(item) == Potion):
            item.amount = item.amount if self.hp + \
                item.amount <= self.max_hp else self.max_hp - self.hp
            self.inventory.remove(item)
            item.on_use()
            self.hp += item.amount
            print(f'\nYou now have {self.hp} health.')
        elif (type(item) == Weapon):
            if(not self.equipped == None):
                self.dmg -= self.equipped.damage
            self.dmg += item.damage
            item.on_equip()
        elif (type(item) == Quest_Item):
            if (self.current_room == item.room):
                print(f'''As you take out the jewel and place it on the pedastal,
the flickering light becomes a pillar of light that shoots
up into the sky, lighting up this dark and damp land.
You can see inside the depths of the chasm - and it\'s
filled with bodies of travellers and adventurers like
yourself that have failed in the quest that you have
just completed.\n\n\tCongratulations!\n
If you got this far, that means you have bested me 
and you are now my adversary. 😂😂''')
                quit()
            else:
                print(
                    f'You can\'t use the {item.name} here. Try somewhere else.')
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

    def take_damage(self, attacker, room):

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

    def attack(self, obj, room):
        obj.take_damage(self, room)

    def block(self, obj, room):
        self.blocking = True
