"""A coffee machine"""
from Menu import MENU, resources


def order_checking(drink_order, order_req):
    """do the order"""
    if drink_order["ingredients"]["water"] > resources["water"]:
        print("There isn't enough water.")
        return False
    elif drink_order["ingredients"]["coffee"] > resources["coffee"]:
        print("There isn't enough coffee.")
        return False
    if order_req != "espresso":
        if drink_order["ingredients"]["milk"] > resources["milk"]:
            print("There isn't enough milk.")
            return False
    return True


def check_money(amount, coffee_type, drink_info):
    """check money"""
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total < amount:
        print(f"There isn't enough money...Money refunded.")
    else:
        if total > amount:
            print(f"Here is your {coffee_type}, enjoy.")
            print(f"change: ${round(total - amount, 2)}")
        else:
            print(f"Here is your {coffee_type}, enjoy.")
        global money
        money += amount
        resources["water"] -= drink_info["ingredients"]["water"]
        resources["coffee"] -= drink_info["ingredients"]["coffee"]
        if coffee_type != "espresso":
            resources["milk"] -= drink_info["ingredients"]["milk"]


money = 0
is_on = True
while is_on:
    order = input("What do u want? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(
            f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}ml\nmoney: ${money}")
    else:
        drink = MENU[order]
        if order_checking(drink, order):
            print("please insert coins.")
            check_money(drink["cost"], order, drink)
    print()
