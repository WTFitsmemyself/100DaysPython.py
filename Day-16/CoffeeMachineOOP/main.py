from menu import Menu, MenuItem
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
    UserInput = input(f"What do you want? {menu.get_items()}: ").lower()
    if UserInput == 'off':
        is_on = False
    elif UserInput == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(UserInput)
        enough = coffee_maker.is_resource_sufficient(item)
        if enough:
            cost_coffee = money_machine.process_coins()
            Ready = money_machine.make_payment(cost_coffee)
            print(Ready)
            
    