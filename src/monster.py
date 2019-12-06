from player import Player


class Monster(Player):

    def __init__(self, name, current_room=None, hp=5, dmg=1):
        super().__init__(name, current_room, dmg, hp)

    def take_damage(self, attacker, room):

        if (not self.blocking):
            self.hp -= attacker.dmg

            if (self.hp <= 0):
                self.change_room(None)
                room.remove_monster_from_room(self)
                print(f'\n{self.name}\'s hp hit 0. {self.name} has died.')

            else:
                print(
                    f'\n{self.name} took {attacker.dmg} damage and now has {self.hp} hit points remaining.')

        else:
            self.blocking = False
            print(f'{self.name} blocked your attack!')

    def change_room(self, room):
        self.current_room = room
