from multiprocessing.connection import Client

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: Prompt user by asking “What would you like?
# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
def coffe_machine():
    is_on = True

    while is_on:
        client_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if client_choice == "off":
            is_on = False
        elif client_choice == "report":
            print_report()
        else:
            drink = MENU[client_choice]
            if check_resources(drink["ingredients"]):
                client_payment = payment()
                if check_transaction(client_choice, client_payment):
                    make_coffee(client_choice)


# TODO 3: Print report
def print_report():
    """ Shows the current resources values."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffe: {resources["coffee"]}g')
    print(f'Money: ${profit}')

# TODO 4: Check resources sufficient
def check_resources(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] > resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True

# TODO 5: Process coins.
def payment():
    """Process the payment"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_payment = quarters + dimes + nickles + pennies

    return total_payment

# TODO 6: Check transaction successful
def check_transaction(client_choice, client_pay):
    """Checks if the transaction was completed"""
    global profit
    if client_pay < MENU[client_choice]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif client_pay == MENU[client_choice]["cost"]:
        profit += client_pay
        resources["Money"] = profit
        return True
    else:
        change = client_pay - MENU[client_choice]["cost"]
        profit += MENU[client_choice]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
        return True

# TODO 7: Make Coffe
"""Prepare the coffee"""
def make_coffee(client_choice):
    for key in MENU[client_choice]["ingredients"]:
        resources[key] -= MENU[client_choice]["ingredients"][key]
    print(f"Here is your {client_choice}. Enjoy!")

coffe_machine()

"""Manipulação de recursos Péssima!"""