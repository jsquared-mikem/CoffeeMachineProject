from menu import MENU, resources, coins
from sys import exit
machine_status = True
money = 0


def needed_resources(drink_type):
    water_needed = MENU[drink_type]["ingredients"]["water"]
    coffee_needed = MENU[drink_type]["ingredients"]["coffee"]

    if "milk" in (MENU[drink_type]["ingredients"]):
        milk_needed = MENU[drink_type]["ingredients"]["milk"]
    else:
        milk_needed = 0
    return water_needed, coffee_needed, milk_needed


def generate_report():
    print(f"Milk: {resources["milk"]}ml")
    print(f"Milk: {resources["water"]}ml")
    print(f"Milk: {resources["coffee"]}g")


def sufficient_supply(ingredients):
    if ingredients[0] > resources["water"]:
        print("Sorry there is not enough water.")
    if ingredients[1] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    if ingredients[2] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def user_coins(pen, nick, dim, quart):
    total = 0
    total += (quart * coins["QUARTER"])
    total += (dim * coins["DIME"])
    total += (nick * coins["NICKEL"])
    total += (pen * coins["PENNY"])
    return total


def enough_funds(user_money, wanted_drink):
    if wanted_drink == "report" or wanted_drink == "off":
        return
    if user_money > MENU[wanted_drink]["cost"]:
        change = user_money - MENU[wanted_drink]["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")
        return MENU[wanted_drink]["cost"]
    elif user_money == MENU[wanted_drink]["cost"]:
        return MENU[wanted_drink]["cost"]
    else:
        return "Sorry that's not enough money. Money refunded"


def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


# TODO: 1. Prompt the user by asking “What would you like? (espresso/latte/cappuccino):”

user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
while machine_status:

    if user_choice == "espresso":
        what_needed = needed_resources(user_choice)

    elif user_choice == "latte":
        what_needed = needed_resources(user_choice)

    elif user_choice == "cappuccino":
        what_needed = needed_resources(user_choice)

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_choice == "off":
        print("Turning Off, have a good one!")
        exit()

    # TODO: 3. Print report.
    elif user_choice == "report":
        generate_report()
        print(f"Money: ${money}")
        exit()
    else:
        print("Drink not available")
        exit()

    # TODO 4. Check resources sufficient?
    is_sufficient_supply = sufficient_supply(what_needed)

    if not is_sufficient_supply:
        exit()

    # TODO 5. Process coins.
    else:
        print("Insert coins.")
        user_quarters = int(input("How many quarters?: "))
        user_dimes = int(input("How many dimes?: "))
        user_nickels = int(input("How many nickels?: "))
        user_pennies = int(input("How many pennies?: "))

        inserted_coins = (user_coins(quart=user_quarters, nick=user_nickels, dim=user_dimes, pen=user_pennies))
        print(inserted_coins)

    # TODO 6. Check transaction successful?
    money += enough_funds(inserted_coins, user_choice)

    # TODO 7. Make Coffee.
    make_coffee(user_choice)
    print(f"Here is your {user_choice}. Enjoy!")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
