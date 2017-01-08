import random

class Player:
    max_hp = 200
    hp = 200

    def __init__(self, atkl, atkh, name):
        self.atkl = atkl
        self.atkh = atkh
        self.name = name

    def get_attack(self):
        return int(random.randrange(self.atkl, self.atkh))

    def print_hp(self):
        print(self.name, "HP is", self.hp)