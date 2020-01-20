# Functions and modular code

Near the end of chapter 3, Sweigart gives us a program that (oddly enough) does not include any functions. It is duplicated here in the file *guess_number_orig.py*.

Let’s *refactor* his program to make it more modular, using functions. *Modular* can mean that each function accomplishes *one* task. Writing a lot of small, short functions gives you an easy way to test and perfect each part of your program in a very manageable way.

**Problem to be solved:** Create a game in which a user gets six tries to guess a random number.

## Pseudo code

It can be very helpful to start your program problem-solving by writing [pseudo code](https://www.youtube.com/watch?v=4G0EYfrrDT8), like this:

1. Get a random number.
2. Ask player to guess it.
3. Check if guess was right.
4. Repeat until either the guess is right or the player runs out of tries.
5. Tell the player the result.

## How to start

Convert your pseudo code into comments, with each comment describing a clear **task** that needs to be completed.

```python
# get random number
# take guesses from user and check each guess
# tell user the result
```

## Build the main function

If you build your main function around your pseudo code, you should be able to make it very modular. *Modular* can mean each function accomplishes one task. It’s not sensible to write a function that contains only one line, so don’t take this too literally.

Let’s begin by including in the main function only code that seems absolutely necessary. Leave out anything that might get complicated.

```python
import random

def guess_number():
    # get random number
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")

    # take guesses from user and check each guess

    # tell user if they won or not

    # this function must tell user the outcome, so: message is returned
    return message
```

“Take guesses from user and check each guess” is two tasks, but you will want to *loop* to ask the user to guess, capture the guess, and then check the guess against the correct answer. You can’t sensibly spit that into two separate functions.

Let’s *name* the two secondary functions and what they return before we write them:

```python
import random

def guess_number():
    # get random number
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")

    # take guesses from user and check each guess
    guesses = take_guesses(secret_number)

    # tell user if they won or not
    message = tell_result(guesses)

    return message
```

Now we know what we have to get out of the `take_guesses()` function: The number of guesses taken. If all guesses were used and none were the correct answer, we know the player failed.

We also know what we have to get out of the `tell_result()` function: The text of a message to the user.

**Think about this:** Knowing what you want to *return* helps you write a better function. Don’t just print things and throw them away. If you *return* something, you can store it in a variable.

## Build a secondary function

Get started like this &mdash; writing out what you need to do:

```python
# compare user input to the secret number
def take_guesses(secret_number):
    # give them 6 guesses
    for i in range(1, 7):
        # ask user for a guess, a number
        # if it's too high, tell them
        # if it's too low, tell them
        # if it's correct, return which guess this is
    return None
```

If they use all six guesses, the loop ends, and you know they never guessed the correct number. You return the `None` value. If they guessed correctly, you return a number: how many tries it took. Below is the completed guessing function.

```python
# compare user input to the secret number
def take_guesses(num):
    # give them 6 guesses
    for i in range(1, 7):
        print("Take a guess.")
        # user enters a number - change string input to integer
        guess = int( input() )
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            # if guess is correct, return number of guesses they took
            return i
    # if they are wrong all times and loop ended -
    return None
```

A great benefit to building modular functions is that you can test them by themselves. [Try out the `take_guesses()` function here.](https://repl.it/@macloo/random-guessing)

## Build another secondary function

Your `take_guesses()` function does the real work of handling the guesses and the comparisons, but it never tells the user anything. That will be done in a separate function. It will return a message (a *string*) for the user.

```python
# tell user if they won or not
message = tell_result(guesses)
```

To know whether the user ever guessed the secret number, you need to pass in the value from the previous function (the parameter `guesses`). That will be either a number from 1 to 6, or the value `None`.

“It will be either this or that” should tip you off that an *if-statement* will work here!

```python
def tell_result(guesses):
    if guesses == None:
        # tell them they never got it right
    else:
        # tell them they guessed the secret number
    return message
```

If you think about the message that will be written out for the user to read, you might realize the loser would like to know *what the secret number was,* and the winner might like to know *how many tries were used.* Add another parameter to the function (to pass in the secret number along with the number of guesses), and you’ve got it:

```python
def tell_result(guesses, number):
    if guesses == None:
        m = "Sorry, you used all your tries. "
        m += "The secret number was " + str(number) + "."
    else:
        m = "Good job! You guessed the number in " + str(guesses) + " tries!"
    return m
```

The file *guess_number_new.py* contains the final, complete program.
