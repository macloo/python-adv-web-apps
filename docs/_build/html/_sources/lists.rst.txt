Working with Lists
==================

This section is based on chapter 4 in Sweigart’s `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

`Python scripts for this section <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/loops_and_lists>`_

Python lists are very similar to JavaScript arrays. However, in Python, an **array** is a different thing, and we will be using lists, not arrays. `Read this if you're curious about the difference. <https://www.pythoncentral.io/the-difference-between-a-list-and-an-array/>`_

A new list can be made like this: ::

    my_list = ['cat', 'bat', 'rat', 'elephant']

As with JavaScript arrays, a Python list contains items that can be accessed via an **index** number. Each item in the list has a unique index, *starting with 0*: ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant']
    >>> print(my_list[1])
    bat
    >>> print(my_list[0])
    cat
    >>>

This next bit is pretty sophisticated, but you will probably use it: We can put **lists *inside* of lists**. When we do, we can access the list items with index numbers as usual, but you’ll need to use one index to access a list (in the list of lists) and a *second* index to access an item inside that list. See Sweigart page 79 for this. It’s like a double-decker list. ::

    >>> new_list = [ [0, 1, 3], ['a', 'b', 'c'], ['red', 'white', 'blue'] ]
    >>> print( new_list[2][0] )
    red
    >>>

Above is an example of a list (`new_list`) that contains three items. Each of the three items is a different list. To access the first item in the third list, we use the index of the third list, `2`, followed by the index of the first item, `0`.

**Slices** provide a way to get several consecutive items from a list all at once; see Sweigart pages 80–81.

The **length** of a list (just like the length of a string) can be found with ``len()``: ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant']
    >>> len(my_list)
    4
    >>> word = "fantastic"
    >>> len(word)
    9
    >>>

Looping over a list
-------------------

Sweigart covers a variety of things we can do to or with Python lists, including adding new items to them and deleting items from them. Perhaps the most common thing we do with lists is **loop through them** to print or inspect their contents: ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant']
    >>> for thing in my_list:
    ...   print(thing)
    ...
    cat
    bat
    rat
    elephant
    >>>

.. attention:: Above, ``thing`` is a new variable. Its value is the value of the current list item. Each time the loop runs, the value of ``thing`` is the *next* item in the list.

If we need to know the index number while we are looping through a list, we can get it with ``enumerate()``: ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant']
    >>> for index, item in enumerate(my_list):
    ...   print('The index: ' + str(index) + ' The item: ' + item)
    ...
    The index: 0 The item: cat
    The index: 1 The item: bat
    The index: 2 The item: rat
    The index: 3 The item: elephant
    >>>

.. attention:: Above, ``index`` and ``item`` are both new variables. The words *index* and *item* are not special. You could just as well use ``a`` and ``b``, or ``i`` and ``thing``.

You don’t need to loop through a list to find out if a particular item exists there. See Sweigart pages 84–85 for details (“The ``in`` and ``not in`` Operators”). He also shows you how to assign list items to individual variables (pages 85–86, “The Multiple Assignment Trick”).

Augmented assignment operators
------------------------------

I have no clue why this is in the middle of the lists chapter, but you should know that in Python we cannot increment a value with ``++`` as we can in JavaScript.

We can, however, use a shortened form instead of ``x = x + 1`` to increment a value: ::

    >>> x = 0
    >>> x += 1
    >>> print(x)
    1
    >>> x += 100
    >>> print(x)
    101
    >>>

The same technique works with ``-``, ``*``, ``\``, and ``%`` (modulus).

Methods, and finding things in lists
------------------------------------

In web scraping, we use a BeautifulSoup *method* on tag objects: ``object.get_text()``

A *method* is a function (e.g. ``get_text()``), but it must be *called on* a *value*. In the ``object.get_text()`` example, ``object`` contains one or more HTML elements and (probably) text. Calling ``get_text()`` on ``object`` returns the text alone, without any HTML tags.

For use with Python lists, Sweigart shows us the *method* ``index()``: If ``spam`` is a Python list and that list contains an item with the value ``"hello"``, then ``spam.index('hello')`` will return the **index number** of that item.

It’s useful to know that if the list *does not* contain that value, then the *method* ``index()`` will return a ``ValueError``. This is useful because (like any error) ``ValueError`` could be used in a ``try``/``except`` combo. When you are scraping, that can be very useful indeed.

Other list methods include ``append()`` and ``insert()``. ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant']
    >>> my_list.append('rhino')
    >>> print(my_list)
    ['cat', 'bat', 'rat', 'elephant', 'rhino']
    >>>

The ``append()`` method is used often in web scraping.

Earlier in the chapter, we saw ``del spam[2]`` — this deletes the item with **index** 2 from the list ``spam``. Note how that is different from the ``remove()`` method: ::

    >>> my_list = ['cat', 'bat', 'rat', 'elephant', 'rhino']
    >>> my_list.remove('bat')
    >>> print(my_list)
    ['cat', 'rat', 'elephant', 'rhino']
    >>>

The ``sort()`` method will only work if your list items are all strings or all numbers. Also, strings that begin with an uppercase letter will be sorted separately from strings that begin with a lowercase letter. ::

    >>> water_list = ['lake', 'Ontario', 'river', 'Hudson', 'ocean', 'Atlantic']
    >>> water_list.sort()
    >>> print(water_list)
    ['Atlantic', 'Hudson', 'Ontario', 'lake', 'ocean', 'river']
    >>>

If you try to use ``.sort()`` on a list that contains both strings and integers, you’ll see this error: ::

    TypeError: '<' not supported between instances of 'str' and 'int'

Note that by using the ``sort()`` method, the list is changed. The old order cannot be regained. The old indexes are destroyed. Originally, ``water_list[0]`` was ``'lake'``. Now it is ``'Atlantic'``.

There is a *method* Sweigart did not cover, and it’s very handy: ``pop()``. We can put an index inside the parentheses, and then the item at that index will be removed, permanently, from the list. If no index is specified, ``pop()`` removes *and returns* the *last* item in the list. Note that leaving the parentheses empty is *the most common way* to use ``pop()``. Here's how it works: ::

    >>> print(water_list)
    ['Atlantic', 'Hudson', 'Ontario', 'lake', 'ocean', 'river']
    >>> water_list.pop()
    'river'
    >>> next_item = water_list.pop()
    >>> another_item = water_list.pop()
    >>> print(water_list)
    ['Atlantic', 'Hudson', 'Ontario']
    >>> print(next_item)
    ocean
    >>> print(another_item)
    lake
    >>>

`Here are all of the methods of Python lists. <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`_

Tuples and immutability
-----------------------

Sweigart explains the difference between *mutable* and *immutable* data types and then goes on to introduce **tuples** (pronounced *too-puls*). A tuple might look like a list at first glance, but it’s not — and it doesn’t behave like a list, either.

A tuple can contain one or more items, like a list, but the items cannot be changed. They cannot be sorted into order, and they cannot be deleted or removed. Perhaps most surprising, you cannot even add a new item to a tuple. Once it is made, a tuple is *immutable*.

Lists are *mutable*, and that means we can change and reorder their contents at any time.

Lists and references
--------------------

Another important thing to know about Python lists is that you can’t simply duplicate one. You might think, “Oh, I’m going to change the contents of ``my_list``, so I’ll make a copy of it as a backup.” This is not going to do what you probably expect: ::

    >>> my_list = ['cat', 'bat', 'rat']
    >>> foobar = my_list
    >>> print(foobar)
    ['cat', 'bat', 'rat']
    >>> # you think you have a copy of my_list in foobar - you are wrong
    >>> my_list.append('aardvark')
    >>> my_list.append('zebra')
    >>> my_list.remove('rat')
    >>> my_list.sort()
    >>> print(my_list)
    ['aardvark', 'bat', 'cat', 'zebra']
    >>> print(foobar)
    ['aardvark', 'bat', 'cat', 'zebra']
    >>>

Sweigart explains this in chapter 4. Both ``my_list`` and ``foobar`` are simply *references* to the list, which exists elsewhere in memory. To make a real copy that is independent of the original, you have to use other means.

Chapter review: chapter 4
-------------------------

Key points
++++++++++

1. Create a new list
2. Get the value of one item in a list using its index
3. Make a double-decker list (lists inside a list) and access specific items in the inner lists.
4. Use slices to get multiple items from a list all at once
5. Use ``len()`` to get the number of items in a list
6. Use ``del()`` to delete an item from a list using its index
7. Loop through a list in different ways
8. Use of ``in`` and ``not in`` with lists
9. Increment a value using ``+=``
10. Use the following *methods* correctly:

   - ``index()``
   - ``append()``
   - ``remove()``
   - ``sort()``
   - ``pop()`` *not in Sweigart; see above*
   
11. The differences between a Python list and a tuple
12. You can’t simply make a copy of a list in the way you might expect (know how to look up the *correct way* to make a copy if you need to do so)

Slides: chapters 9 and 4
++++++++++++++++++++++++

`Slide deck <http://bit.ly/pythonrev3>`_
