msg_0 = "Starting to make a coffee"
msg_1 = "Grinding coffee beans"
msg_2 = "Boiling water"
msg_3 = "Mixing boiled water with crushed coffee beans"
msg_4 = "Pouring coffee into the cup"
msg_5 = "Pouring some milk into the cup"
msg_6 = "Coffee is ready!"
msg_7 = "Write how many cups of coffee you will need:"
msg_8 = "Write how many {measurement} of {ingredient} the coffee machine has:"
msg_9 = "The coffee machine has:"
msg_10 = "Write action (buy, fill, take, remaining, exit): "
msg_11 = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "

EXPRESSO_WATER_PER_CUP = 250
EXPRESSO_MILK_PER_CUP = 0
EXPRESSO_COFFEE_BEANS_PER_CUP = 16
EXPRESSO_PRICE_PER_CUP = 4

LATTE_WATER_PER_CUP = 350
LATTE_MILK_PER_CUP = 75
LATTE_COFFEE_BEANS_PER_CUP = 20
LATTE_PRICE_PER_CUP = 7

CAPPUCCINO_WATER_PER_CUP = 200
CAPPUCCINO_MILK_PER_CUP = 100
CAPPUCCINO_COFFEE_BEANS_PER_CUP = 12
CAPPUCCINO_PRICE_PER_CUP = 6

coffee_machine_water, coffee_machine_milk, coffee_machine_coffee_beans = 0, 0, 0
coffee_machine_cups, coffee_machine_money = 0, 0


def init_coffee_machine_status():
    global coffee_machine_water, coffee_machine_milk, coffee_machine_cups, coffee_machine_coffee_beans, \
        coffee_machine_money

    coffee_machine_water = 400
    coffee_machine_milk = 540
    coffee_machine_coffee_beans = 120
    coffee_machine_cups = 9
    coffee_machine_money = 550


def display_coffee_machine_status():
    print(msg_9)
    print(f"""{coffee_machine_water} ml of water
{coffee_machine_milk} ml of milk
{coffee_machine_coffee_beans} ml of coffee beans
{coffee_machine_cups} g of disposable cups
${coffee_machine_money} of money""")


def get_coffee_machine_ingredient(ingredient):
    print(msg_8.replace("{ingredient}", ingredient).replace("{measurement}",
                                                            "ml" if ingredient in ["water", "milk"] else "grams"))
    return int(input())


def check_ingredients_for_coffee(water, milk, coffee_bean, coffee_price):
    global coffee_machine_water, coffee_machine_milk, coffee_machine_cups, coffee_machine_coffee_beans, \
        coffee_machine_money

    enough_resources = True
    if water > coffee_machine_water:
        enough_resources = False
        print("Sorry, not enough water!")
        return

    if milk > coffee_machine_milk:
        enough_resources = False
        print("Sorry, not enough milk!")
        return

    if coffee_machine_cups == 0:
        enough_resources = False
        print('Sorry, not enough cup!')
        return

    if coffee_bean > coffee_machine_coffee_beans:
        enough_resources = False
        print("Sorry, not enough coffee beans!")
        return

    if enough_resources:
        print("I have enough resources, making you a coffee!")
        coffee_machine_water -= water
        coffee_machine_milk -= milk
        coffee_machine_cups -= 1
        coffee_machine_coffee_beans -= coffee_bean
        coffee_machine_money += coffee_price


def buy_action():
    print()
    print(msg_11)
    item_to_buy = input()

    if item_to_buy == "back":
        return customer_action()
    elif int(item_to_buy) == 1:
        check_ingredients_for_coffee(EXPRESSO_WATER_PER_CUP, EXPRESSO_MILK_PER_CUP, EXPRESSO_COFFEE_BEANS_PER_CUP,
                                     EXPRESSO_PRICE_PER_CUP)
    elif int(item_to_buy) == 2:
        check_ingredients_for_coffee(LATTE_WATER_PER_CUP, LATTE_MILK_PER_CUP, LATTE_COFFEE_BEANS_PER_CUP,
                                     LATTE_PRICE_PER_CUP)
    elif int(item_to_buy) == 3:
        check_ingredients_for_coffee(CAPPUCCINO_WATER_PER_CUP, CAPPUCCINO_MILK_PER_CUP, CAPPUCCINO_COFFEE_BEANS_PER_CUP,
                                     CAPPUCCINO_PRICE_PER_CUP)
    return


def fill_action():
    global coffee_machine_water, coffee_machine_milk, coffee_machine_cups, coffee_machine_coffee_beans, \
        coffee_machine_money
    coffee_machine_water += get_coffee_machine_ingredient("water")
    coffee_machine_milk += get_coffee_machine_ingredient("milk")
    coffee_machine_coffee_beans += get_coffee_machine_ingredient("coffee_beans")
    print("Write how many disposable coffee cups you want to add:")
    coffee_machine_cups += int(input())


def customer_action():
    global coffee_machine_money

    while True:
        print(msg_10)
        action = input()

        if action == "exit":
            exit()
        elif action == "remaining":
            print()
            display_coffee_machine_status()
            print()
        elif action == "take":
            coffee_machine_money -= coffee_machine_money
            print(f"I gave you ${coffee_machine_money}")
            print()
        elif action == "fill":
            fill_action()
        elif action == "buy":
            buy_action()
            print()


init_coffee_machine_status()

customer_action()

# def get_ingredients(nb_drinks):
#     water = nb_drinks * WATER_PER_CUP
#     milk = nb_drinks * MILK_PER_CUP
#     bean = nb_drinks * COFFEE_BEANS_PER_CUP
#     print(
#         f"""For {nb_drinks} cups of coffee you will need:\
#         {water} ml of water
#         {milk} ml of milk
#         {bean} g of coffee beans""")
#     return water, milk, bean
#
#
