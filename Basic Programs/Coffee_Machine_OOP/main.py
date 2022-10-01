from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_bank = MoneyMachine()
is_machine_on = True
while is_machine_on:
    user_choice = input(f"Whay would you like to have? ({menu.get_items()}) ")
    # print(user_choice)
    if user_choice.upper() == "OFF":
        is_machine_on = False
    elif user_choice.upper() == "REPORT":
        coffeemaker.report()
        money_bank.report()

    # print(drink)
    else:
        drink = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(drink):
            # print(coffeemaker.is_resource_sufficient(drink))
            if money_bank.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
