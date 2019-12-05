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

    def add_item_to_room(self, item):
        self.item_list.append(item)

    def remove_item_from_room(self, item):
        self.item_list.remove(item)

    def has_item(self, item):
        return item in self.item_list

    def has_items(self):
        return len(self.item_list) > 0
