# example of badly using scope of variables

def breakfast():
    food = 'eggs'
    drink = 'coffee'
    print("Breakfast:")
    print(food, drink, "\n")

def lunch():
    food = 'salad'
    drink = 'iced tea'
    print("Lunch:")
    print(food, drink, "\n")

# run the functions
lunch()
breakfast()

# attempt to print local variables (will not work)
print(food)
print(drink)
