from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    clear()
    UserInput = input(f"What do you want? {menu.get_items()}: ").lower()
    if UserInput == 'off':
        is_on = False
    elif UserInput == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(UserInput)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
