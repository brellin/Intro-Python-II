class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')


class Potion(Item):

    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def on_use(self):
        print(f'{self.name} heals you for {self.amount} hit points. Now it\'s empty.')
