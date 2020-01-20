# this is a revised version of Sweigart's "guess the number" game, pp. 74-76

import random

maximum_secret_number = 30

# generate a random number and check it against guesses
# this is the main function - note, it runs the other two functions in this file
def guess_number(top):
    secret_number = random.randint(1, top)
    print("I'm thinking of a number between 1 and " + str(top) + ".")
    # take guesses from user
    guesses = take_guesses(secret_number)
    # tell user if they won or not
    message = tell_result(guesses, secret_number)
    return message

# compare user input to the secret number
def take_guesses(num):
    # give them 6 guesses
    for i in range(1, 7):
        print("Take a guess.")
        guess = int( input() )
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            # if guess is correct
            return i
    # if they are wrong all times and loop ended -
    return None

# give a different message depending on whether they guessed correctly
def tell_result(g, n):
    if g == None:
        m = "Sorry, you used all your tries. "
        m += "The secret number was " + str(n) + "."
    else:
        m = "Good job! You guessed the number in " + str(g) + " tries!"
    return m

# run the main function
result = guess_number(maximum_secret_number)
print(result)
