Functions in Python
===================

This section is based on chapter 3 in Sweigart’s `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

`Python scripts for this section <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/functions>`_

Write and run a Python script
-----------------------------

To write functions in Python, you will be saving files with the `.py` extension. You can write and save Python files in `Atom <https://atom.io/>`_ or in `Mu <https://codewith.mu/en/about>`_.

To run a script named `foobar.py` that’s in the current directory, type this at the bash prompt (`$`) in Mac or the Windows Command Prompt: ::

   python3 foobar.py

On Windows, or in a *virtualenv* on Mac or Windows, drop the ``3`` from ``python3``.

You do not need to be in your *virtualenv* to do this, but it’s okay if you are.

Put something in, get something out
-----------------------------------

Sweigart notes that many functions operate as “black boxes”: This describes a function with parameters (it takes arguments) and a `return` statement. Something goes into it (arguments) and something comes out of it (whatever is returned). You don’t need to know how it works; you just need to know what it does.

*a_black_box.py* ::

   def add_things(a, b):
      result = (a * 3) + (b * 3)
      return result

To run that function, *call it,* passing in two strings as arguments: ::

   add_things("love", "Gators")

The function will *return* this: ::

   loveloveloveGatorsGatorsGators

However, you will not *see* the returned value *unless* you capture it, or “catch” it, with a variable, like this: ::

   output = add_things("love", "Gators")

Then you can print `output` or send it to a database or write it into the HTML of a live web page — or whatever you need. ::

   print(output)

This is true for many functions we use from imported libraries. We know how to *call* the function, and we know what to expect as output, but we don’t need to know how it works.

We don’t need to know how a toaster toasts bread to get toast out of it. We put in two pieces of bread (the *arguments* we pass into a function), and toast is *returned* after the function runs.

Using parameters and returns in functions
-----------------------------------------

Let’s build a function step by step to help you understand parameters and returns. Assume that you buy the same coffee (or other beverage) daily, and you want to calculate how much you spend per week.

.. literalinclude:: ../python_code_examples/functions/b_function_demo_1.py

It’s not very useful like that. What if the price of the drink changes? What if you want to calculate a different time period?

.. literalinclude:: ../python_code_examples/functions/c_function_demo_2.py

Now you're able to *pass in* any price and any time span you want. However, you can’t use the value for `total` if there’s no `return` statement. So — return the total amount spent on coffee.

.. literalinclude:: ../python_code_examples/functions/d_function_demo_3.py

The function is good, but the way you *call* it needs to change. To assign the *returned value* of a function to a new variable, follow this pattern:

.. literalinclude:: ../python_code_examples/functions/e_function_demo_4.py

A function can have many lines of instructions inside its code block (including conditionals, loops, and more).

It’s best to write functions that perform one specific task, rather than several tasks.

Scope
-----

This is a bit of a hard topic for beginners, because you don’t have much experience writing longer or complex scripts.

Consider the following example:

.. literalinclude:: ../python_code_examples/functions/f_scope_global_vs_local.py
   :caption:

Everything will work fine *except the last two lines.* If you run the script, you’ll see what the two functions print: ::

   Lunch:
   salad iced tea

   Breakfast:
   eggs coffee

But then you'll see an error: ::

   Traceback (most recent call last):
      File "f_scope_global_vs_local.py", line 20, in <module>
         print(food)
   NameError: name 'food' is not defined

The error message (last line) clearly states the problem: You tried to print the value of the variable ``food``, but there is no such variable *outside the functions.* The script stopped with ``print(food)``, but if you tried ``print (drink)`` instead, you’d get the same error.

Note that it’s fine to have ``food`` in both functions and ``drink`` in both functions — there is no conflict or confusion because of local scope.

Key points about scope
++++++++++++++++++++++

- A variable has *local* scope or *global* scope. It cannot have both.
- A local variable exists only *inside* a function. It cannot be transmitted outside the function (although its *value* can be — via `return`).
- Sometimes you will make a mistake about the scope of a variable, and then you will get an error — or (worse) your answers or results will not be correct.
- A global variable exists *outside* any function. It may be used inside a function.
- “It is a **bad habit** to rely on global variables as your programs get larger and larger” (Sweigart, p. 66).
- **Avoid** repeating the names of variables in different scopes. If you have a global variable named `foobar`, do not name a local variable `foobar`.
- See four rules, p. 69 in Sweigart

try/except
----------

When your program throws an error, your script stops. In most cases you want to be informed of the error but *not* have the script come to a halt. The usual way to accomplish this in Python is to write the code you want to run within the ``try`` block, and write instructions for handling the error inside the ``except`` block.

.. literalinclude:: ../python_code_examples/functions/h_try_except.py
   :caption:

The code above requires the user to type a whole number. A string or a decimal (float) will trigger the exception.

To find out what kind of error would be thrown, experiment at the Python command line (error types are case sensitive). Also, there is a list of `built-in exceptions <https://docs.python.org/3/library/exceptions.html>`_.

Chapter review: chapter 3
-------------------------

These are the takeaways from this chapter. Slides below.

Key points
++++++++++

1. The `def` statement (how and where to use it)
2. *When* is the code in a function executed? (Know the difference between *defining* a function and *running* it.)
3. Parameters or arguments: Where are these, in a function?

   - How do they work when you *define* the function?
   - How do they work when you *run* the function? (*Note:* Instead of *run,* we may say *call* or *execute* the function. All have the same meaning.)

4. The `return` keyword (used in a function)
5. The `NoneType` data type: value is `None`

   - This will be important in scraping! If you get an error that says something does not work because it cannot be applied to `NoneType`, it means something returned `None` when you were expecting another value.
   - “Python adds `return None` to the end of any function definition with no `return` statement” (Sweigart, p. 62). In other words, a function with no `return` statement returns `None`.
   - An empty `return` statement (that is, the word `return` alone on a line) also returns `None`.

6. Keyword arguments: You can forget this for the time being
7. **Important!** Scope of variables
8. Functions as “black boxes”: Describes a function with *parameters* (meaning that it takes *arguments*) and a `return` statement. One or more values go into the function (arguments) and some value comes out of it (whatever is returned).
9. Exception handling (also called error handling): `try`/`except` pattern

Slides: chapter 3
+++++++++++++++++

`Python Review 2 <http://bit.ly/pythonrev2>`_
