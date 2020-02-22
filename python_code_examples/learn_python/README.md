# About these files

These Python scripts are based on [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (second edition), chapters 1 and 2. All of the code is explained in those two chapters.

It is recommended that you **run the files** in the Terminal. Run them multiple times until you understand exactly what each line in the code does.

## Chapter 1

**Script:** *a_tiny_script.py*

This interactive program says hello and asks you to type your name and age. It assigns your name and age to variables. It then uses the variables to print out strings, which will differ depending on what you responded.

These Python **built-in functions** are demonstrated in the interactive program:

- ``print()``
- ``input()``
- ``len()``
- ``int()``
- ``str()``

## Chapter 2

**Script:** *b_if_statements.py*

This interactive program also asks you to type your name and age. Depending on the values you enter, different responses will be printed. You should try to make each of the four different responses appear, and recognize how each expression (the "condition") is *evaluated* as `True` or `False` by Python.

The four conditions:

1. the value of name is 'Alice' and the age is less than 13
2. the value of name is 'Alice' (and the age is *not* less than 13)
3. the age is less than 13 (and the name is *not* 'Alice')
4. any other combination (e.g. name is 'Fred' and age is 14)

Note that the **order** of the statements matters.

**Script:** *c_while_loop.py*

- Students often struggle to understand while-loops. This one asks you to `Type the word spam`. You should run it and type a word *other than* "spam," and also run it and type "spam." Study the code until you understand why `Spam spam spam spam` prints and also why `No more spam 😥` prints.

**Script:** *d_while_break_continue.py*

- A while-loop may contain a `break` statement, a `continue` statement, or both, or neither. This example from [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) is very clear in demonstrating how these two statements work, but you'll need to run it multiple times and type "Joe" and other names, as well as "swordfish" and other passwords, to understand it.

**Script:** *e_for_loops.py*

- This script demonstrates four different for-loops that all use `range()`. This is not the only pattern for using a for-loop in Python, but it's the only pattern that's covered in chapter 2.

- It would be good for you to practice some of these for-loops in the interactive Python shell. Experiment with using one, two, or three **arguments** inside the parentheses.

- Notice how **starting with 0** or **starting with 1** affects the final number shown in the first and fourth for-loops here.

**Script:** *f_random.py*

This is the most complex script in this group. It includes:

- The `import` statement
- Use of `random.randint()` to generate random numbers
- A while-loop
- A set of control-flow statements
- A Python list (these are covered in chapter 4)
- An `input()` statement to let the user decide whether the while-loop continues or not (only typing "q" will stop the loop)

Can you see how one random number determines the card's value (Ace, 1, 2 ... Queen, or King) and the *other* random number determines the card's suit?
