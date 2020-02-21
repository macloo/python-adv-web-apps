Dictionaries
============

This section is based on chapter 5 in Sweigart’s `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

- `Python scripts for this section <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/dictionaries>`_

- `Python documentation for dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

Introduction to dictionaries
----------------------------

The crucial concept to understand is that a **dictionary** consists of *key-value pairs*. ::

    { "Title": "Harry Potter and the Goblet of Fire", "Author": "J. K. Rowling", "Year": 2001 }

The **keys** in that dictionary are ``"Title"``, ``"Author"`` and ``"Year"``.

The **values** in that dictionary are ``"Harry Potter and the Goblet of Fire"``, ``"J. K. Rowling"`` and ``2001``.

Different from a **list**, a dictionary does not have indexes. You can’t depend on the *order* of items in a dictionary to stay the same. You cannot insert a new item into a particular position in a dictionary because the items do not have positions, or places. Thus we refer to **lists** as *ordered* and to dictionaries as *unordered*.

Although Sweigart refers to the keys as *indexes,* you shouldn't think of them behaving exactly as indexes do in lists.

To understand Python dictionaries better, run the file *simple_dict.py* found `here <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/dictionaries/>`_.

Note that **keys** can be strings, integers or floats, and **values** can also be strings, integers or floats. ::

    >>> new_dict = {}
    >>> new_dict['name'] = 'Mahatma Gandhi'
    >>> new_dict[2] = 'India'
    >>> new_dict[3.14] = 'chakras'
    >>> new_dict['number'] = 108
    >>> new_dict['one'] = 1
    >>> print(new_dict)
    {'name': 'Mahatma Gandhi', 2: 'India', 3.14: 'chakras', 'number': 108, 'one': 1}
    >>>

Other data types can also be used as dictionary values, as you’ll see below.


How to loop over a dictionary
-----------------------------

The following ways to loop through a dictionary are demonstrated in the file `looping_keys_values.py <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/dictionaries/looping_keys_values.py>`_. Run it to see how it works.

* ``for k in dict.keys():``
* ``for v in dict.values():``
* ``for k, v in dict.items():``

Naturally, your dictionary likely will not be named ``dict``.

Sweigart does an excellent job of explaining dictionaries in chapter 5.

You can get a Python **list** of all the keys in a dictionary: ::

    keys_list = list(dict.keys())

Similarly, you can get a Python **list** of all the values: ::

    values_list = list(dict.values())

Converting a CSV to a dictionary
--------------------------------

You can use Python’s ``csv`` module and the ``DictReader()`` method to create a list of dictionaries from a CSV file (also see *dictreader_example2.py* `here <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/dictionaries/>`_).

.. literalinclude:: ../python_code_examples/dictionaries/dictreader_example.py
   :caption:

Note that if you try to treat a DictReader object like a normal list, it will not work: ::

    >>> print(my_reader)
    <csv.DictReader object at 0x1047c5400>

But you can *convert* the DictReader object into a normal list if needed: ::

    new_list_version = list(my_reader)
    >>> print(new_list_version)
    [{'Title': 'The Calculating Stars', 'Author': 'Mary Robinette Kowal', 'Year': '2019'}, {'Title': 'The Stone Sky', 'Author': 'N. K. Jemisin', 'Year': '2018'}, {'Title': 'The Obelisk Gate', 'Author': 'N. K. Jemisin', 'Year': '2017'}, {'Title' ...

Writing a dictionary into a CSV file
------------------------------------

This is covered in the `CSV Files chapter <csv.html#writing-from-a-dictionary>`_.

Converting JSON to a dictionary or vice versa
---------------------------------------------

This is covered in the `CSV chapter <csv.html#json-formatted-data>`_.

Examples of complex dictionaries
--------------------------------

This is a bit like the nesting Matryoshka dolls from Russia — you can combine multiple dictionaries in a list, and you can even nest dictionaries inside other dictionaries.

A list of dictionaries
++++++++++++++++++++++

In this data structure, one Python list contains many dictionaries. Each dictionary is a list item.

All the dictionaries contain the same keys. ::

    presidents_list = [
    {"Presidency":1,"President":"George Washington","Wikipedia_entry":"http://en.wikipedia.org/wiki/George_Washington","Took_office":"4/30/1789","Left_office":"3/4/1797","Party":"Independent ","Home_state":"Virginia","Occupation":"Planter","College":"None","Age_when_took_office":57,"Birth_date":"2/22/1732","Birthplace":"Westmoreland County, Virginia","Death_date":"12/14/1799","Location_death":"Mount Vernon, Virginia"},
    {"Presidency":2,"President":"John Adams","Wikipedia_entry":"http://en.wikipedia.org/wiki/John_Adams","Took_office":"3/4/1797","Left_office":"3/4/1801","Party":"Federalist ","Home_state":"Massachusetts","Occupation":"Lawyer","College":"Harvard","Age_when_took_office":61,"Birth_date":"10/30/1735","Birthplace":"Quincy, Massachusetts","Death_date":"7/4/1826","Location_death":"Quincy, Massachusetts"},
    {"Presidency":3,"President":"Thomas Jefferson","Wikipedia_entry":"http://en.wikipedia.org/wiki/Thomas_Jefferson","Took_office":"3/4/1801","Left_office":"3/4/1809","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Planter, Lawyer","College":"William and Mary","Age_when_took_office":57,"Birth_date":"4/13/1743","Birthplace":"Albemarle County, Virginia","Death_date":"7/4/1826","Location_death":"Albemarle County, Virginia"},
    {"Presidency":4,"President":"James Madison","Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Madison","Took_office":"3/4/1809","Left_office":"3/4/1817","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"Princeton","Age_when_took_office":57,"Birth_date":"3/16/1751","Birthplace":"Port Conway, Virginia","Death_date":"6/28/1836","Location_death":"Orange County, Virginia"},
    {"Presidency":5,"President":"James Monroe","Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Monroe","Took_office":"3/4/1817","Left_office":"3/4/1825","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"William and Mary","Age_when_took_office":58,"Birth_date":"4/28/1758","Birthplace":"Westmoreland County, Virginia","Death_date":"7/4/1831","Location_death":"New York, New York"}
    ]


A dictionary of dictionaries
++++++++++++++++++++++++++++

In this data structure, one dictionary contains key-value pairs in which the value *for each key* is a dictionary.

Here the **key** is the name of a U.S. president and its **value** is a dictionary containing facts about that president. Note where the curly braces are used. ::

    presidents_dict = {
    "George Washington": {"Presidency":1,"Wikipedia_entry":"http://en.wikipedia.org/wiki/George_Washington","Took_office":"4/30/1789","Left_office":"3/4/1797","Party":"Independent ","Home_state":"Virginia","Occupation":"Planter","College":"None","Age_when_took_office":57,"Birth_date":"2/22/1732","Birthplace":"Westmoreland County, Virginia","Death_date":"12/14/1799","Location_death":"Mount Vernon, Virginia"},
    "John Adams": {"Presidency":2,"Wikipedia_entry":"http://en.wikipedia.org/wiki/John_Adams","Took_office":"3/4/1797","Left_office":"3/4/1801","Party":"Federalist ","Home_state":"Massachusetts","Occupation":"Lawyer","College":"Harvard","Age_when_took_office":61,"Birth_date":"10/30/1735","Birthplace":"Quincy, Massachusetts","Death_date":"7/4/1826","Location_death":"Quincy, Massachusetts"},
    "Thomas Jefferson": {"Presidency":3,"Wikipedia_entry":"http://en.wikipedia.org/wiki/Thomas_Jefferson","Took_office":"3/4/1801","Left_office":"3/4/1809","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Planter, Lawyer","College":"William and Mary","Age_when_took_office":57,"Birth_date":"4/13/1743","Birthplace":"Albemarle County, Virginia","Death_date":"7/4/1826","Location_death":"Albemarle County, Virginia"},
    "James Madison": {"Presidency":4,"Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Madison","Took_office":"3/4/1809","Left_office":"3/4/1817","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"Princeton","Age_when_took_office":57,"Birth_date":"3/16/1751","Birthplace":"Port Conway, Virginia","Death_date":"6/28/1836","Location_death":"Orange County, Virginia"},
    "James Monroe": {"Presidency":5,"Wikipedia_entry":"http://en.wikipedia.org/wiki/James_Monroe","Took_office":"3/4/1817","Left_office":"3/4/1825","Party":"Democratic-Republican ","Home_state":"Virginia","Occupation":"Lawyer","College":"William and Mary","Age_when_took_office":58,"Birth_date":"4/28/1758","Birthplace":"Westmoreland County, Virginia","Death_date":"7/4/1831","Location_death":"New York, New York"}
    }

Chapter review: chapter 5
-------------------------

Key points
++++++++++

1. Differences between lists and dictionaries
2. Take care with use of quotes when both keys and values are strings
3. How to loop through keys, values, or both at once
4. Use ``list( dict.keys() )`` to get a list of all keys in a dictionary
5. Check for presence of a key or a value with ``in`` or ``not in``
6. Provide a default value in case a key is not present: ``dict.get(key, value)``
7. Use ``dict.setdefault(key, value)`` to set a new key but prevent overwriting an existing value if the key is already present
8. Use ``import pprint`` if you need to print out a large dictionary’s contents in the Terminal

In the section “Using Data Structures to Model Real-World Things,” Sweigart discusses nested dictionaries and lists. This is illustrated above with the example shown under the subheading “A dictionary of dictionaries.”


Slides: chapters 5 and 16
+++++++++++++++++++++++++

`Python Review 4 <http://bit.ly/pythonrev4>`_

.
