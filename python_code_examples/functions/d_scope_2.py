# example 2 of badly using scope of variables

# global variables are outside all functions
food = "pizza"
drink = "beer"

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

# print global variables - note, they have not changed
print(food)
print(drink)
