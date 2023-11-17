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

profit = 0

def check_resources_sufficiency(coffee):
    for key in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    print("Please enter coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)


def check_transaction_successful(coffee, money_given_by_customer):
    if MENU[coffee]["cost"] <= money_given_by_customer:
        if MENU[coffee]["cost"] < money_given_by_customer:
            print(
                f"Here is ${round(money_given_by_customer-MENU[coffee]['cost'], 2)} in change.")
        return True
    else:
        print(f"Sorry, you don't have enough money. Money Refunded.")
        False


def update_resources(coffee):
    global profit
    for key in MENU[coffee]["ingredients"]:
        resources[key] = resources[key] - \
            MENU[coffee]["ingredients"][key]

    profit += MENU[coffee]["cost"]


def make_coffee(coffee):
    print(f"Here is your {coffee} ☕. Enjoy!")


def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "espresso" or choice == "cappuccino" or choice == "latte":
        if check_resources_sufficiency(choice):
            money_given_by_customer = process_coins()
            if check_transaction_successful(choice, money_given_by_customer):
                update_resources(choice)
                make_coffee(choice)
    elif choice == "report":
        show_report()
    elif choice == "off":
        break
    else:
        print("Invalid Input")
