from abc import ABC


class Item(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description
