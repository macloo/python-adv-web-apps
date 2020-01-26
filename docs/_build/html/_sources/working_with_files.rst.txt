Reading and Writing Files
=========================

This section is based on chapter 9 in Sweigart’s `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

`Python scripts for this section <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/working_with_files>`_

Python can access files on your computer. It can create new text files and write into them. It can also read text files and copy text from them.

In Sweigart’s chapter 9, we are mainly interested in pages 215–219, “The File Reading/Writing Process.” Nevertheless, the previous section in chapter 9, under “Files and File Paths,” does contain useful information. I suggest you scan through the chapter up to page 215 and then read pages 215–219 carefully.

The ``pathlib`` module can be a bit confusing. `You can learn more here. <https://realpython.com/python-pathlib/>`_

Most students will benefit from a review of “Absolute vs. Relative Paths” (pages 206–207).

.. attention:: Be sure to note the differences between paths on Mac and paths on Windows. If you write Python code meant for others to use, and your code includes a reference to a path, then you should use the ``pathlib`` module to ensure that your code for a path would work on both Mac and Windows.

Check whether a file exists
---------------------------

The ``pathlib`` method ``.exists()`` is useful if your Python program needs to check for the existence of a file in the current directory on your computer: ::

    >>> import pathlib
    >>> path = pathlib.Path('foobar.txt')
    >>> path.exists()
    False
    >>>

If ``False`` is returned, no file with that name exists in that location.

Read a file line by line
------------------------

Sweigart explains the ``readlines()`` method (page 218), but he does not cover the ``readline()`` method, which reads exactly *one* line at a time. These two different methods can come in handy for solving different problems.

In the following example, first we write two new lines into a new file. Then we read them, one at a time, with ``readline()``: ::

    >>> myfile = open('temp.txt', 'w')
    >>> myfile.write('hello my little file\n')
    21
    >>> myfile.write('goodbye my little file\n')
    23
    >>> myfile.close()
    >>> myfile = open('temp.txt')
    >>> print( myfile.readline() )
    hello my little file

    >>> print( myfile.readline() )
    goodbye my little file

    >>> myfile.close()
    >>>

Compare that with this example, using ``readlines()``: ::

    >>> myfile = open('temp.txt')
    >>> print( myfile.readlines() )
    ['hello my little file\n', 'goodbye my little file\n']
    >>> myfile.close()
    >>>

When you call ``readlines()`` on a file, it returns a Python **list** that contains each line in the file as a list item. You can then loop over the list, search the items, sort them, etc.

There's a method Sweigart does not cover, ``seek()``. This comes in handy if you have a file open for reading and you have come to the bottom of it. Calling ``seek(0)`` on the File object returns to the *top* of the file so you can read it or search its contents again. ::

    >>> myfile = open('temp.txt')
    >>> myfile.readlines()          # file has been read top to bottom
    >>> print( myfile.readline() )  # nothing happens

    >>> myfile.seek(0)              # return to top
    0
    >>> print( myfile.readline() )  # try again
    hello my little file

    >>> myfile.close()
    >>>

Open and read a file, write to another file
-------------------------------------------

In this example, we have a plain-text file that contains four items of information about each U.S. state, one line per state. In each line, the four items are separated by tabs.

Our task is to use that file, *state_data.txt,* to create a new file, *capitals.txt,* that has only a list of state capitals. So we want to get this:

.. figure:: _static/images/capitals.png
  :scale: 50 %
  :alt: screenshot of capitals file

From this:

.. figure:: _static/images/state_data.png
   :scale: 50 %
   :alt: screenshot of state_data file

Here's how we can do that:

.. literalinclude:: ../python_code_examples/working_with_files/readlines_example.py
   :caption:

An alternative way to open a file
---------------------------------

This opens a File object — ``f`` — for appending, writes to it, closes it and saves it, without using ``close()``. `Read more about it here. <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`_ ::

    with open('temp.txt', 'a') as f:
    	words = "I would not like to eat any spam."
    	f.write(words)

That code would open a file named *myfile.txt* for *appending* — ``a`` — and assign the File object to the variable ``f``. It would write the string into *myfile.txt* and then save and close the file.

If this alternative makes sense to you, feel free to use it instead of using ``f = open('temp.txt')`` etc.

.. important:: The indentation after the ``with`` line is *essential.* Any code related to the open file must be inside the indented block, or you will get errors.

Chapter review: chapter 9
-------------------------

Key points
++++++++++

1. Ways to use the ``pathlib`` module.
2. Use of the ``pathlib`` method ``.exists()``.
3. Files can be opened and read without using ``Path`` if they are in the same folder as the Python script.
4. Call the ``open()`` function to return a File object
5. Call the ``read()`` or ``write()`` method on a File object
6. Close the file by calling the ``close()`` method on a File object — this also *saves* the file
7. Distinguish between the File object and the *contents* of the file
8. Call the ``readlines()`` method to create a **list** from a file that contains line breaks
9. The difference between the ``readline()`` method and the ``readlines()`` method
10. The difference between *write* mode — ``'w'`` — and *append* mode — ``'a'`` — when using ``open()``
11. Use of the alternative syntax ``with open('temp.txt', 'a') as f:``

Slides: chapters 9 and 4
++++++++++++++++++++++++

`Slide deck <http://bit.ly/pythonrev3>`_
