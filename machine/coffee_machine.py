msg_0 = "Starting to make a coffee"
msg_1 = "Grinding coffee beans"
msg_2 = "Boiling water"
msg_3 = "Mixing boiled water with crushed coffee beans"
msg_4 = "Pouring coffee into the cup"
msg_5 = "Pouring some milk into the cup"
msg_6 = "Coffee is ready!"
msg_7 = "Write how many cups of coffee you will need:"
msg_8 = "Write how many {measurement} of {ingredient} the coffee machine has:"

WATER_PER_CUP = 200
MILK_PER_CUP = 50
COFFEE_BEANS_PER_CUP = 15


def get_coffee_machine_ingredient(ingredient):
    print(msg_8.replace("{ingredient}", ingredient).replace("{measurement}",
                                                            "ml" if ingredient in ["water", "milk"] else "grams"))
    return int(input())


def get_ingredients(nb_drinks):
    water = nb_drinks * WATER_PER_CUP
    milk = nb_drinks * MILK_PER_CUP
    bean = nb_drinks * COFFEE_BEANS_PER_CUP
    print(
        f"""For {nb_drinks} cups of coffee you will need:\
        {water} ml of water
        {milk} ml of milk
        {bean} g of coffee beans""")
    return water, milk, bean


def get_nb_of_cups_by_ingredients(water, milk, coffee_beans):
    nb_cups_by_water = water // WATER_PER_CUP
    nb_cups_by_milk = milk // MILK_PER_CUP
    nb_cups_by_coffee_beans = coffee_beans // COFFEE_BEANS_PER_CUP
    if min(nb_cups_by_water, nb_cups_by_milk, nb_cups_by_coffee_beans) > 0:
        return min(nb_cups_by_water, nb_cups_by_milk, nb_cups_by_coffee_beans)
    else:
        return 0


coffee_machine_water, coffee_machine_milk, coffee_machine_coffee_beans = \
    get_coffee_machine_ingredient("water"), \
    get_coffee_machine_ingredient("milk"), \
    get_coffee_machine_ingredient("coffee beans")

print(msg_7)

nb_of_cups_user_wants = int(input())
nb_of_cups_possible = get_nb_of_cups_by_ingredients(coffee_machine_water, coffee_machine_milk,
                                                    coffee_machine_coffee_beans)
if nb_of_cups_user_wants == nb_of_cups_possible:
    print("Yes, I can make that amount of coffee")
elif nb_of_cups_user_wants > nb_of_cups_possible:
    print(f"No, I can make only {nb_of_cups_possible} cups of coffee")
else:
    print(
        f"Yes, I can make that amount of coffee (and even {nb_of_cups_possible - nb_of_cups_user_wants} more than that)")
