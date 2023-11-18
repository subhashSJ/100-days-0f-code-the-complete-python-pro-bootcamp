from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        item = menu.find_drink(choice)

        if item != None:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
