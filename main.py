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


def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no {item} left")
            return False
        return True


def process_coins():
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies")) * 0.01
    return total


def check_transaction(money_recieved, drink_ordered):
    if money_recieved >= drink_ordered:
        change = round(money_recieved - drink_ordered, 2)
        print(f"Your change is ${change}")
        global profit
        profit += drink_ordered
        return True
    else:
        print(f"Sorry that isnt enough, Your money has been refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What coffee would you like? espresso/ latte/ cappuccino? ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])


