import re
import random
from modules.core_math import *

print("Console Calculator")
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


def check_list_index(list, index):
    print(list[index])


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

a_value = 260
reduce_low = 60
reduce_high = 80

while a_value > 0:
    reduction = random.randrange(reduce_low, reduce_high)
    a_value -= reduction

    if a_value <= 0:
        a_value = 0

    print("Value reduced by", reduction, "New value is", a_value)

    if a_value != 0:
        continue

    print("Lowest allowed value reached, exiting program...")
