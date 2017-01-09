from classes.colours import Colours
from classes.person import Person

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


def battle():
    player = Person(460, 65, 60, 34, magic)
    enemy = Person(1200, 65, 45, 25, magic)
    running = True

    print(Colours.FAIL + Colours.BOLD + "AN ENEMY ATTACKS!" + Colours.ENDC)

    while running:
        print("======================")
        player.choose_action()
        index = int(input("Choose action:")) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(player.generate_damage())
            print("You attacked for", dmg, "points of melee damage. Enemy HP:", enemy.get_hp())
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1
            magic_dmg = player.generate_spell_damage(magic_choice)
            spell = player.get_spell_name(magic_choice)
            cost = player.get_spell_mp_cost(magic_choice)

            current_mp = player.get_mp()

            if cost > current_mp:
                print(Colours.FAIL + "\nNot enough MP.\n" + Colours.ENDC)
                continue

            player.reduce_mp(cost)
            enemy.take_damage(magic_dmg)
            print(Colours.OKBLUE + "\n" + spell, "Deals,", str(magic_dmg), "points of damage." + Colours.ENDC)

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print(Colours.FAIL + "Enemy attacks for", enemy_dmg, "points of melee damage." + Colours.ENDC)

        print("\nEnemy HP:", Colours.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Colours.ENDC + "\n")
        print("Your HP:", Colours.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Colours.ENDC)
        print("Your MP:", Colours.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Colours.ENDC + "\n")

        if enemy.get_hp() == 0:
            print(Colours.OKGREEN + "You win!" + Colours.ENDC)
            running = False
        elif player.get_hp() == 0:
            print((Colours.FAIL + "You enemy has defeated you!" + Colours.ENDC))
            running = False
