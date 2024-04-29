from menu import Menu
from coins import Coins
from coffee_maker import Coffee_Maker
menu = Menu()

coffee_maker = Coffee_Maker()
process_on = True
while process_on:
    user = input("What would you like? espresso/latte/cappuccino")
    if user == "espresso" or user == "latte" or user == "cappuccino":
        gen = menu.data(user)
        if coffee_maker.resource_check(gen) is True:
            coins = Coins(gen)
            if coins.input_coins() is True:
                coffee_maker.coffee_machine(gen)
    elif user == "report":
        coffee_maker.report()
