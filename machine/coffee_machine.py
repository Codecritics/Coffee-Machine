msg_0 = "Starting to make a coffee"
msg_1 = "Grinding coffee beans"
msg_2 = "Boiling water"
msg_3 = "Mixing boiled water with crushed coffee beans"
msg_4 = "Pouring coffee into the cup"
msg_5 = "Pouring some milk into the cup"
msg_6 = "Coffee is ready!"
msg_7 = "Write how many cups of coffee you will need:"
WATER_PER_DRINK = 200
MILK_PER_DRINK = 50
BEAN_PER_DRINK = 15


def get_ingredients(nb_drinks):
    water = nb_drinks * WATER_PER_DRINK
    milk = nb_drinks * MILK_PER_DRINK
    bean = nb_drinks * BEAN_PER_DRINK
    print(
        f"""For {nb_drinks} cups of coffee you will need:\
        {water} ml of water
        {milk} ml of milk
        {bean} g of coffee beans""")
    return water, milk, bean


# print(msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, sep="\n")

print("Write how many cups of coffee you will need:")
nb_cups = int(input())
get_ingredients(nb_cups)
