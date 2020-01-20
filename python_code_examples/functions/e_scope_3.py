# example 3 of badly using scope of variables
# this can be very confusing (and cause trouble) because we use
# the variable names food and drink both inside and outside of functions
# we actually have 2 DIFFERENT variables with the name food and
# 2 DIFFERENT variables with the name drink

# global variables are outside all functions
food = "pizza"
drink = "beer"

# local variable food
def food(meal):
    if meal == "breakfast":
        food = 'eggs'
    elif meal == "lunch":
        food = 'salad'
    else:
        food = None
    return food

# local variable drink
def drink(meal):
    if meal == "breakfast":
        drink = 'coffee'
    elif meal == "lunch":
        drink = 'iced tea'
    else:
        drink = None
    return drink

# run the functions and store what is returned, changing
# the value of both global variables
food = food("lunch")
drink = drink("breakfast")

# print global variables - note, now they have changed
print("The current food: " + food)
print("The current drink: " + drink)
