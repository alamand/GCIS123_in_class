# 11.1.7
class Fruit:
    type = 'Unknown'
    price = 0.0


APPLE = Fruit ()
APPLE.type = "Apple"
APPLE.price = 1.25

PEAR = Fruit ()
PEAR.type = "Pear"
PEAR.price = 1.35

GRAPES = Fruit ()
GRAPES.type = "Grapes"
GRAPES.price = 2.95

# 11.1.8
def add_to_basket (fruit, basket):
    if fruit == APPLE.type.lower ():
        basket.append (APPLE)
    elif fruit == PEAR.type.lower ():
        basket.append (PEAR)
    elif fruit == GRAPES.type.lower ():
        basket.append (GRAPES)
    elif fruit == '':
        pass
    else:
        print ("Unknown Fruit")


# 11.1.9
def calculate_cost (basket):
    cost = 0
    for fruit in basket:
        cost += fruit.price

    return cost

def count_fruit (fruit, basket):
    count = 0
    for item in basket:
        if item == fruit:
            count += 1

    return count


def main ():
    basket = []
    selection = None
    while selection != '':
        selection = input ("Which fruit would you like: ")
        add_to_basket (selection, basket)

    cost = calculate_cost (basket)
    apple_count = count_fruit (APPLE, basket)
    pear_count = count_fruit (PEAR, basket)
    grapes_count = count_fruit (GRAPES, basket)

    print ("Thank you for purchasing:", apple_count, "Apples,",
            pear_count, "Pears,", "and", grapes_count, "Grapes.")
    print ("That comes to $", round (cost, 2))

if __name__ == '__main__':
    main ()