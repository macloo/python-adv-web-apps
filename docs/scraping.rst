Web Scraping Intro
==================

This document assumes you have already installed Python 3, and you have used both *pip* and *venv*. If not, refer to `these instructions <http://bit.ly/install-python3-jupyter>`_.

Sweigart briefly covers scraping in chapter 12 of `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

BeautifulSoup documentation:

* `A nicely formatted PDF <https://media.readthedocs.org/pdf/beautiful-soup-4/latest/beautiful-soup-4.pdf>`_
* `The official docs <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_

Setup for BeautifulSoup
-----------------------

**BeautifulSoup** is a scraping library for Python. We want to run all our scraping projects in a virtual environment, so we will set that up first. (Students have already installed Python 3.)

Create a directory and change into it
+++++++++++++++++++++++++++++++++++++

The first step is to create a new folder (directory) for all your scraping projects. Mine is: ::

    Documents/python/scraping

**Do not use any spaces in your folder names.** If you must use punctuation, do not use anything other than an underscore ``_``. It’s best if you use only lowercase letters.

**Change into that directory.** For me, the command would be: ::

    cd Documents/python/scraping

Create a new virtualenv in that directory and activate it
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Create** a new *virtual environment* there (this is done only once).

MacOS: ::

    python3 -m venv env

Windows: ::

    python -m venv env

**Activate** the *virtual environment*:

MacOS: ::

    source env/bin/activate

Windows: ::

    env\Scripts\activate.bat

**Important:** You should now see ``(env)`` at the far left side of your prompt. This indicates that the *virtual environment* is active. For example (MacOS): ::

    (env) mcadams scraping $

When you are *finished* working in a virtual environment, you should **deactivate** it. The command is the same in MacOS or Windows (DO **NOT** DO THIS NOW): ::

    deactivate

You’ll know it worked because ``(env)`` will no longer be at the far left side of your prompt.

Install the BeautifulSoup library
+++++++++++++++++++++++++++++++++

In MacOS or Windows, at the command prompt, type: ::

    pip install beautifulsoup4

This is how you install *any* Python library that exists in the `Python Package Index <https://pypi.python.org/pypi>`_. Pretty handy. **pip** is a tool for installing Python packages, which is what you just did.

.. note:: You have installed BeautifulSoup in the Python virtual environment that is currently active. When that virtual environment is *not* active, BeautifulSoup will not be available to you. This is ideal, because you will create different virtual environments for different Python projects, and you won’t need to worry about updated libraries in the future breaking your (past) code.

Test BeautifulSoup
------------------

**Start Python.** Because you are already in a Python 3 virtual environment, Mac users need only type ``python`` (NOT ``python3``). Windows users also type ``python`` as usual.

You should now be at the ``>>>`` prompt — the Python interactive shell prompt.

In MacOS or Windows, type (or copy/paste) *one line at a time*: ::

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
    soup = BeautifulSoup(page, "html.parser")
    print(soup.h1)

1. You imported two Python modules, ``urlopen`` and ``BeautifulSoup`` (the first two lines).
2. You used ``urlopen`` to copy the entire contents of the URL given into a new Python variable, ``page`` (line 3).
3. You used the ``BeautifulSoup`` *function* to process the value of that variable (the plain-text contents of the file at that URL) through a built-in HTML parser called ``html.parser``.
4. The result: All the HTML from the file is now in a BeautifulSoup object with the new Python variable name ``soup``. (It is just a variable name.)
5. Last line: Using the syntax of the BeautifulSoup library, you printed the first ``h1`` element (including its tags) from that parsed value.

If it works, you'll see: ::

    <h1>We Are Learning About Web Scraping!</h1>

Check out `the page on the web <https://weimergeeks.com/examples/scraping/example1.html>`_ to see what you scraped.

.. attention:: If you got an error about SSL, quit Python (``quit()`` or Command-D) and COPY/PASTE this at the command prompt (MacOS only): ::

        /Applications/Python\ 3.8/Install\ Certificates.command

    Then return to the Python prompt and retry the five lines above.

The command ``soup.h1`` would work the same way for any HTML tag (if it exists in the file). Instead of printing it, you might stash it in a variable: ::

    heading = soup.h1

Then, to see the text in the element without the tags: ::

    print(heading.text)


Understanding BeautifulSoup
---------------------------

BeautifulSoup is a Python library that enables us to extract information from web pages and even entire websites.

We use BeautifulSoup commands to create a well-structured data *object* (more about objects below) from which we can extract, for example, everything with an ``<li>`` tag, or everything with ``class="book-title"``.

After extracting the desired information, we can use other Python commands (and libraries) to write the data into a database, CSV file, or other usable format — and then we can search it, sort it, etc.

What is the BeautifulSoup object?
+++++++++++++++++++++++++++++++++

It’s  important to understand that many of the BeautifulSoup commands work on an *object,* which is not the same as a simple *string.*

Many programming languages include objects as a data type. Python does, JavaScript does, etc. An *object* is an even more powerful and complex data type than an *array* (JavaScript) or a *list* (Python) and can contain many other data types in a structured format.

When you extract information from an *object* with a BeautifulSoup command, sometimes you get a single **tag object,** and sometimes you get a Python *list* (similar to an *array* in JavaScript) of tag objects. The way you treat that extracted information will be **different** depending on whether it is *one* item or a list (usually, but not always, containing *more than one* item).

That last paragraph is **REALLY IMPORTANT,** so read it again.

How BeautifulSoup handles the object
++++++++++++++++++++++++++++++++++++

In the previous code, when this line ran: ::

    page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")

... you copied the *entire contents of a file* into a new Python variable named ``page``. The contents were stored as an *HTTPResponse object*. We can read the contents of that object like this:

.. figure:: _static/images/url_blob.png
   :scale: 40 %
   :alt: Results of html.read() screenshot

... but that’s not going to be very usable, or useful — especially for a file with a lot more content in it.

When you transform that *HTTPResponse object* into a *BeautifulSoup object* — with the following line — you create a well-structured object from which you can extract *any HTML element* and the text and/or attributes *within* any HTML element. ::

    soup = BeautifulSoup(page, "html.parser")


Some basic BeautifulSoup commands
---------------------------------

Let’s look at a few examples of what BeautifulSoup can do.

Finding elements that have a particular class
+++++++++++++++++++++++++++++++++++++++++++++

Deciding the best way to extract what you want from a large HTML file requires you to dig around in the source before you write the Python/BeautifulSoup commands. In many cases, you’ll see that everything you want has the same **CSS class** on it. After creating a *BeautifulSoup object* (here, as before, it is ``soup``), this line will create a Python *list* containing all the ``<td>`` elements that have the class ``city``. ::

    city_list = soup.find_all( "td", class_="city" )

.. attention:: The word *class* is a **reserved word** in Python. Using *class* (alone) in the code above would give you a syntax error. So when we search by CSS class with BeautifulSoup, we use the keyword argument ``class_`` with an *underscore* added. Other HTML attributes DO NOT need the underscore.

Maybe there were 10 cities in ``<td>`` tags in that HTML file. Maybe there were 10,000. No matter how many, they are now in a *list* (assigned to the variable ``city_list``), and you can search them, print them, write them out to a database or a JSON file — whatever you like. Often you will want to perform the same actions on each item in the list, so you will use a normal Python *for-loop*: ::

    for city in city_list:
        print( city.get_text() )

``get_text()`` is a handy BeautifulSoup method that will extract the text — and only the text — from the item. If instead you wrote just ``print(city)``, you’d get the ``<td>`` and any other tags inside that as well.

Finding all vs. finding one
+++++++++++++++++++++++++++

The BeautifulSoup ``find_all()`` method you just saw always produces a *list*. (Note: ``findAll()`` will also work.) If you know there will be only one item of the kind you want in a file, you should use the ``find()`` method instead.

For example, maybe you are scraping the address and phone number from every page in a large website. There is only one phone number on the page, and it is enclosed in a pair of tags with the attribute ``id="call"``. One line of your code gets the phone number from the current page: ::

    phone_number = soup.find(id="call")

Naturally, you don’t need to loop through that result — the variable ``phone_number`` will contain only a string, including any HTML tags. To test what the text alone will look like, just print it using ``get_text()`` to strip out the tags. ::

    print( phone_number.get_text() )

Notice that you’re always using ``soup``. Review above if you’ve forgotten where that came from. (You may use another variable name instead, but ``soup`` is the usual choice.)

Finding the contents of a particular attribute
++++++++++++++++++++++++++++++++++++++++++++++

One last example from `the example page <https://weimergeeks.com/examples/scraping/example1.html>`_ we have been using.

Say you’ve made a BeautifulSoup object from a page that has dozens of images on it. You want to capture *the path to each image file* on that page (perhaps so that you can download all the images). This requires two steps: ::

    image_list = soup.find_all('img')
    for image in image_list:
        print(image.attrs['src'])

First, you make a Python *list* containing all the ``img`` elements that exist in the object.

Second, you loop through that list and print the contents of the ``src`` attribute from each ``img`` tag in the list.

.. important:: We do not need ``get_text()`` in this case, because the contents of the ``src`` attribute (or any HTML attribute) are nothing but text. There are never tags inside the ``src`` attribute. So *think* about *exactly* what you’re trying to get, and what is it like inside the HTML of the page.

There’s a lot more to learn about BeautifulSoup, and we’ll be working with various examples. You can always `read the docs <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_. Most of what we do with BeautifulSoup, though, involves these tasks:

- Find everything with a particular class
- Find everything with a particular attribute
- Find everything with a particular HTML tag
- Find one thing on a page, often using its ``id`` attribute
- Find one thing that’s inside another thing

A BeautifulSoup scraping example
--------------------------------

To demonstrate a whole process of thinking through a small scraping project, I made a `Jupyter Notebook <soup_practice.ipynb>`_ that shows how I broke down the problem step by step, and tested one thing at a time, to reach the solution I wanted. Open the notebook here on GitHub to follow along and see all the steps.

The code in the *final cell* of the notebook produces `this 51-line CSV file <movies.csv>`_ by scraping 10 separate web pages.

To *run* the notebook, you will need to have installed the `Requests <https://requests.readthedocs.io/en/master/>`_ module and also Jupyter Notebook. ::

    pip install requests
    pip install jupyter

See `these instructions <http://bit.ly/install-python3-jupyter>`_ for information about how to run Jupyter Notebooks.
