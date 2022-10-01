from _ast import While

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

money_earned = 0
is_transaction_successful = True
are_items_sufficient = True


def check_item(a):
    global are_items_sufficient
    for item in MENU[a]['ingredients']:
        if (MENU[a]['ingredients'][item]) >= resources[item]:
            print(f"There is no sufficient amount of {item}")
            are_items_sufficient = False
    # print(are_items_sufficient)
    return are_items_sufficient


def check_coins():
    global is_transaction_successful
    global money_earned
    quarter_coins = int(input("enter the number of quarters ")) * 0.25
    dime_coins = int(input("enter the number of dimes ")) * 0.1
    nickles_coins = int(input("enter the number of nickles ")) * 0.05
    pennie_coins = int(input("enter the number of pennies ")) * 0.01
    user_cash = quarter_coins + dime_coins + nickles_coins + pennie_coins
    if user_cash < MENU[user_choice]["cost"]:
        print("sorry! this amount is not sufficient")
    is_transaction_successful = False
    money_earned += MENU[user_choice]["cost"]
    if user_cash > MENU[user_choice]["cost"]:
        balance = round(user_cash - MENU[user_choice]["cost"], 2)
        print(f"Here is your {balance} change")
    return is_transaction_successful


def make_coffee(a):
    for item in MENU[a]['ingredients']:
        resources[item] = (resources[item] - MENU[a]['ingredients'][item])
    print(f"Please enjoy your {a}")


is_machine_on = True
while is_machine_on:
    user_choice = input("What coffee would like to have?: ")
    if user_choice.upper() == "OFF":
        is_machine_on = False
        print("the machine is turned off")
    elif user_choice.upper() == "REPORT":
        print(f"water   :   {resources['water']} ml")
        print(f"milk    :   {resources['milk']} ml")
        print(f"coffee  :   {resources['coffee']} g")
        print(f"profit  :   ${money_earned}")

    if is_machine_on and user_choice.upper() != "REPORT":
        check_item(user_choice)
        # print(are_items_sufficient)
        if is_machine_on and user_choice.upper() != "REPORT" and are_items_sufficient:
            check_coins()
        else:
            is_machine_on = False
            print("Please refill")
        if is_transaction_successful := True and user_choice.upper() != "REPORT" and is_machine_on:
            make_coffee(user_choice)

