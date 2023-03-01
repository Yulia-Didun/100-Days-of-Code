from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def coffee_machine():
    continue_serving = True

    while continue_serving:
        options = menu.get_items()
        user_choice = input(f"  What would you like? ({options}): ")

        if user_choice == 'off':  # continue serving coffee till user inputs 'off'
            return

        elif user_choice == 'report':  # prints a report on the available resources
            coffee_maker.report()
            money_machine.report()

        else:
            drink = menu.find_drink(user_choice)
            if not coffee_maker.is_resource_sufficient(drink) or not money_machine.make_payment(drink.cost):
                # if there's not enough ingredients, start again
                return coffee_machine()

            else:
                coffee_maker.make_coffee(drink)


money = 0
coffee_machine()
