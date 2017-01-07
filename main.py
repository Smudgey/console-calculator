import re
from modules.core_math import *

print("Console Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def print_math_results():
    print(add(7, 5))
    print(subtract(7, 5))
    print(multiply(7, 5))
    print(divide(7, 5))


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
