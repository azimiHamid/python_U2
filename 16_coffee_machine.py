from utils_16.menu import Menu, MenuItem
from utils_16.coffee_maker import CoffeeMaker
from utils_16.money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


MENU = {}
for item in menu.menu:
    MENU[item.name] = item


def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

is_on = True
while is_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = MENU[choice]
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)