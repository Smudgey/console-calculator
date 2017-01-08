from classes.colours import Colours
from classes.person import Person

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 40}]


def battle():
    player = Person(460, 65, 60, 34, magic)
    enemy = Person(1200, 65, 45, 25, magic)
    running = True

    print(Colours.FAIL + Colours.BOLD + "AN ENEMY ATTACKS!" + Colours.ENDC)

    while running:
        print("======================")
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(player.generate_damage())
            print("You attacked for", dmg, "points of melee damage. Enemy HP:", enemy.get_hp())

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg, "points of melee damage. Player HP:", player.get_hp())
