# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item_list = list()
        self.monster_list = list()

    def add_item_to_room(self, item):
        self.item_list.append(item)

    def remove_item_from_room(self, item):
        self.item_list.remove(item)

    def add_monster_to_room(self, monster):
        self.monster_list.append(monster)
        monster.change_room(self)

    def remove_monster_from_room(self, monster):
        self.monster_list.remove(monster)
        monster.change_room(None)

    def has_item(self, item):
        return item in self.item_list

    def has_monster(self, monster):
        return monster in self.monster_list

    def print_contents(self):
        if (len(self.item_list) > 0):
            condS = 's' if len(self.item_list) > 1 else ''
            print(f'Item{condS} in {self.name}:')
            for item in self.item_list:
                print(f'\t{item.name}: {item.description}')
        else:
            print(f'There are no items in {self.name}.')

        if (len(self.monster_list) > 0):
            for monster in self.monster_list:
                print(f'\n{monster.name} is in the room!')
        else:
            print(f'There are no monsters in {self.name}.')
