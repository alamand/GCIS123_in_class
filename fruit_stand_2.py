# 11.2.5
class Fruit:
    __slots__ = ['type', 'price', 'count']
    def __init__ (self, type, price):
        self.type = type
        self.price = price
        self.count = 0


FRUITS = {'apple' :Fruit ('Apple' , 1.25), 
          'pear'  :Fruit ('Pear'  , 1.35),
          'grapes':Fruit ('Grapes', 2.95)}

def add_to_basket (fruit, basket):
    fruit = fruit.lower ()
    if fruit in FRUITS:
        basket += [FRUITS [fruit]]
    elif fruit == '':
        pass
    else:
        print ("Sorry, we don't sell ", fruit, "'s.", sep = '')

def calculate_cost (basket):
    cost = 0
    for fruit in basket:
        cost += fruit.price
        fruit.count += 1

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

    # Feel free to put this into a loop, was being lazy due to formatting
    print ("Thank you for purchasing:", FRUITS['apple'].count, "Apples,",
            FRUITS['pear'].count, "Pears,", "and", FRUITS['grapes'].count, "Grapes.")
    print ("That comes to $", round (cost, 2), sep = '')

if __name__ == '__main__':
    main ()    