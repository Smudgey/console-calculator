import re
import random
from modules.core_math import *


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh, name):
        self.atkl = atkl
        self.atkh = atkh
        self.name = name

    def get_attack(self):
        return int(random.randrange(self.atkl, self.atkh))

    def print_hp(self):
        print(self.name, "HP is", self.hp)


class Player:
    hp = 200

    def __init__(self, atkl, atkh, name):
        self.atkl = atkl
        self.atkh = atkh
        self.name = name

    def get_attack(self):
        return int(random.randrange(self.atkl, self.atkh))

    def print_hp(self):
        print(self.name, "HP is", self.hp)

print("Python Intro")
print("Type 'quit' to exit\n")

previous = 0
run = True
my_list = ["One", "Two",
           "Three", "Four",
           "Five", "Six"]


def print_math_results():
    print(add(7, 5))
    print(subtract(7, 5))
    print(multiply(7, 5))
    print(divide(7, 5))


def check_list_index(a_list, index):
    print(a_list[index])


def validate_equation(equation):
    re.sub('[a-zA-Z,.:()" "]', '', equation)


def perform_math():
    global run
    global previous

    if previous == 0:
        equation = input("Enter an equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        validate_equation(equation)
        """print_math_results()"""

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()

print_math_results()
check_list_index(my_list, 4)

player1 = Player(120, 150, "Player 1")
enemy1 = Enemy(40, 50, "Enemy 1")
enemy2 = Enemy(75, 90, "Enemy 2")

while player1.hp > 0:
    reduction = enemy1.get_attack() + enemy2.get_attack()
    player1.hp -= reduction

    if player1.hp <= 0:
        player1.hp = 0

    print("HP reduced by", reduction, "New value is", player1.hp)

    if player1.hp != 0:
        continue

    print("You have died, exiting program...")
