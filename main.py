import re
from modules.game import battle
from modules.quit import quit_operations

print("Python Intro")
print("Type 'quit' to exit\n")

previous = 0
run = True
equation = ""


def validate_equation(eq):
    re.sub('[a-zA-Z,.:()" "]', '', eq)


def perform_math():
    global run
    global previous
    global equation

    if previous == 0:
        equation = input("Enter an equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit' or equation == 'rpg':
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

if equation == 'quit':
    quit_operations()
elif equation == 'rpg':
    battle()
