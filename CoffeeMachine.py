MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
keep_making_coffee = True


def report():
    """"Display current resources within machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources(drink_choice):
    """Verify sufficient resources for beverage"""
    if drink_choice == "espresso":
        if resources["water"] > 50:
            if resources["coffee"] > 18:
                return True
            else:
                print("Sorry, there is not enough coffee.")
                return False
        else:
            print("Sorry, there is not enough water.")
            return False
    elif drink_choice == "latte":
        if resources["water"] > 200:
            if resources["milk"] > 150:
                if resources["coffee"] > 24:
                    return True
                else:
                    print("Sorry, there is not enough coffee.")
                    return False
            else:
                print("Sorry, there is not enough milk.")
                return False
        else:
            print("Sorry, there is not enough water.")
            return False
    elif drink_choice == "cappuccino":
        if resources["water"] > 250:
            if resources["milk"] > 100:
                if resources["coffee"] > 24:
                    return True
                else:
                    print("Sorry, there is not enough coffee.")
                    return False
            else:
                print("Sorry, there is not enough milk.")
                return False
        else:
            print("Sorry, there is not enough water.")
            return False
    else:
        return False


def process_coins(drink_choice):
    """ if enough, take money from user and return change if needed"""
    global money
    change = 0
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = pennies + nickles + dimes + quarters
    if drink_choice == "espresso":
        if total >= 1.50:
            change = round(total - 1.50, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that is not enough money. Money refunded.")
            return False
    elif drink_choice == "latte":
        if total >= 2.50:
            change = round(total - 2.50, 2)
            print(f"Here is {change} in change.")
            return True
        else:
            print("Sorry, that is not enough money. Money refunded.")
            return False
    elif drink_choice == "cappuccino":
        if total >= 3.00:
            change = round(total - 3.00, 2)
            print(f"Here is {change} in change.")
            return True
        else:
            print("Sorry, that is not enough money. Money refunded.")
            return False


def make_coffee(drink_choice):
    """remove resources and add money for drink"""
    global money
    if drink_choice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        money += 1.50
        print(f"Here's your {drink_choice} ☕. Enjoy!")
    elif drink_choice == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        money += 2.50
        print(f"Here's your {drink_choice} ☕. Enjoy!")
    elif drink_choice == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        money += 3.00
        print(f"Here's your {drink_choice} ☕. Enjoy!")


def turn_off_machine():
    exit()


def coffee_machine():
    while keep_making_coffee:
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_choice == "off":
            turn_off_machine()
        elif drink_choice == "report":
            report()
        else:
            if check_resources(drink_choice) and process_coins(drink_choice):
                make_coffee(drink_choice)


coffee_machine()
