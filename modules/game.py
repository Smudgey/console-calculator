from classes.colours import Colours
from classes.person import Person

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 40}]


def battle():
    player = Person(460, 65, 60, 34, magic)

    print(player.generate_damage())
    print(player.generate_spell_damage(0))
    print(player.generate_spell_damage(1))
    print(player.generate_damage())
