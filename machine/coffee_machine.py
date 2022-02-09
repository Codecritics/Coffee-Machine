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
msg_10 = "Write action (buy, fill, take):"
msg_11 = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"

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
    print(f"""{coffee_machine_water} of water
{coffee_machine_milk} of milk
{coffee_machine_coffee_beans} of coffee beans
{coffee_machine_cups} of disposable cups
{coffee_machine_money} of money""")


def get_coffee_machine_ingredient(ingredient):
    print(msg_8.replace("{ingredient}", ingredient).replace("{measurement}",
                                                            "ml" if ingredient in ["water", "milk"] else "grams"))
    return int(input())


def buy_action():
    global coffee_machine_water, coffee_machine_milk, coffee_machine_cups, coffee_machine_coffee_beans, \
        coffee_machine_money
    print(msg_11)
    item_to_buy = int(input())

    if item_to_buy == 1:
        coffee_machine_water -= EXPRESSO_WATER_PER_CUP
        coffee_machine_milk -= EXPRESSO_MILK_PER_CUP
        coffee_machine_cups -= 1
        coffee_machine_coffee_beans -= EXPRESSO_COFFEE_BEANS_PER_CUP
        coffee_machine_money += EXPRESSO_PRICE_PER_CUP
    elif item_to_buy == 2:
        coffee_machine_water -= LATTE_WATER_PER_CUP
        coffee_machine_milk -= LATTE_MILK_PER_CUP
        coffee_machine_cups -= 1
        coffee_machine_coffee_beans -= LATTE_COFFEE_BEANS_PER_CUP
        coffee_machine_money += LATTE_PRICE_PER_CUP
    elif item_to_buy == 3:
        coffee_machine_water -= CAPPUCCINO_WATER_PER_CUP
        coffee_machine_milk -= CAPPUCCINO_MILK_PER_CUP
        coffee_machine_cups -= 1
        coffee_machine_coffee_beans -= CAPPUCCINO_COFFEE_BEANS_PER_CUP
        coffee_machine_money += CAPPUCCINO_PRICE_PER_CUP


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
    print(msg_10)
    action = input()
    while action not in ["buy", "fill", "take"]:
        customer_action()
    if action == "take":
        coffee_machine_money -= coffee_machine_money
        print(f"I gave you ${coffee_machine_money}")
    elif action == "fill":
        fill_action()
    elif action == "buy":
        buy_action()


init_coffee_machine_status()
display_coffee_machine_status()
print()
customer_action()
print()
display_coffee_machine_status()


def does_coffee_machine_can_do_enough_coffee():
    if nb_of_cups_user_wants == nb_of_cups_possible:
        print("Yes, I can make that amount of coffee")
    elif nb_of_cups_user_wants > nb_of_cups_possible:
        print(f"No, I can make only {nb_of_cups_possible} cups of coffee")
    else:
        print(
            f"Yes, I can make that amount of coffee (and even {nb_of_cups_possible - nb_of_cups_user_wants} more than that)")

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
# def get_nb_of_cups_by_ingredients(water, milk, coffee_beans):
#     nb_cups_by_water = water // WATER_PER_CUP
#     nb_cups_by_milk = milk // MILK_PER_CUP
#     nb_cups_by_coffee_beans = coffee_beans // COFFEE_BEANS_PER_CUP
#     if min(nb_cups_by_water, nb_cups_by_milk, nb_cups_by_coffee_beans) > 0:
#         return min(nb_cups_by_water, nb_cups_by_milk, nb_cups_by_coffee_beans)
#     else:
#         return 0
