from data import MENU, resources


def report(resources):
    """Print the resources report."""
    global money
    for resource, amount in resources.items():
        if resource == 'coffee':
            print(f"{resource.title()}: {amount}g")
        else:
            print(f"{resource.title()}: {amount}ml")
    print(f"Money: ${money}")


def check_resources_sufficient(coffee, resources, menu):
    """Checks whether there are enough ingredients to make the coffee."""
    coffee_requirements = menu[coffee]['ingredients']

    if 'water' in coffee_requirements:
        if coffee_requirements['water'] > resources['water']:
            print("Sorry, there is not enough water.")
            return False

    if 'milk' in coffee_requirements:
        if coffee_requirements['milk'] > resources['milk']:
            print("Sorry, there is not enough milk.")
            return False

    if 'coffee' in coffee_requirements:
        if coffee_requirements['coffee'] > resources['coffee']:
            print("Sorry, there is not enough coffee.")
            return False

    return True


def process_coins():
    """Ask user to insert coins. Returns sum in dollars."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    return quarters + dimes + nickles + pennies


def check_transaction(coffee, menu, inserted_coins):
    """Checks whether user inserted enough money for chosen coffee."""
    global money
    cost = menu[coffee]['cost']
    if inserted_coins < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_coins >= cost:
        money += cost
        inserted_coins -= cost
        print(f"Here is ${round(inserted_coins, 2)} in charge.")
        return True


def make_coffee(coffee, resources, menu):
    """'Serves' coffee and reduces used ingredients from resources."""
    print(f"Here is your {coffee} ☕. Enjoy!")
    coffee_requirements = menu[coffee]['ingredients']

    if 'water' in coffee_requirements:
        resources['water'] -= coffee_requirements['water']

    if 'milk' in coffee_requirements:
        resources['milk'] -= coffee_requirements['milk']

    if 'coffee' in coffee_requirements:
        resources['coffee'] -= coffee_requirements['coffee']


def coffee_machine():
    continue_serving = True

    while continue_serving:
        user_choice = input("  What would you like? (espresso, latte, cappuccino): ")

        if user_choice == 'off':  # continue serving coffee till user inputs 'off'
            return

        elif user_choice == 'report':  # prints a report on the available resources
            report(resources)

        else:
            if not check_resources_sufficient(user_choice, resources, MENU):
                # if there's not enough ingredients, start again
                return coffee_machine()

            else:  # otherwise ask user to insert coins
                inserted_coins = process_coins()
                if not check_transaction(user_choice, MENU, inserted_coins):
                    # if there is not enough money, start over
                    return coffee_machine()
                else:  # if there is enough money, make a coffee
                    make_coffee(user_choice, resources, MENU)


money = 0
coffee_machine()