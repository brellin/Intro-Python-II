class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.droppable = True

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')


class Potion(Item):

    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount
        self.droppable = True

    def on_use(self):
        print(f'{self.name} heals you for {self.amount} hit points. Now it\'s empty.')


class Weapon(Item):

    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
        self.droppable = True

    def on_equip(self):
        self.droppable = False
        print(
            f'You equip {self.name}. {self.name} gives you +{self.damage} damage!')


class Quest_Item(Item):

    def __init__(self, name, description, room):
        super().__init__(name, description)
        self.room = room
        self.droppable = False

    def on_take(self):
        print(f'{self.name} is a quest item. Hang onto it.')

    def on_drop(self):
        print(f'{self.name} is a QUEST ITEM. You cannot drop it.')
