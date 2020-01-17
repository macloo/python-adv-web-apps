import random

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
    # convert the number to a string
    card = str(card)

# this is a list, which is very much like an array
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# we use the index of a list item just as we do in Javascript
# so we get a random suit 
suit = suits[suit]

print('You drew the ' + card + ' of ' + suit + '.')
