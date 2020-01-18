import random

# set value for the while-loop
answer = ""

while answer != 'q':
    # get 2 random numbers
    card = random.randint(1,13)
    suit = random.randint(0,3)

    # use an if-statement to name the cards
    if card == 1:
        card = "Ace"
    elif card == 11:
        card = "Jack"
    elif card == 12:
        card = "Queen"
    elif card == 13:
        card = "King"
    else:
        # convert any other number to a string
        card = str(card)

    # this is a list, much like an array in JavaScript
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    # we use the index of a list item just as we do in Javascript
    # so we get a random suit
    suit = suits[suit]

    print('You drew the ' + card + ' of ' + suit + '.\n')

    # user chooses whether to draw another card - only q will stop the loop
    print("Draw a new card?")
    answer = input("Press Enter/Return to continue or q to quit.\n")

# continue here after while-loop is finished
print("\nThanks for playing!\n")
