Web Scraping, Part 2
====================

You have installed **BeautifulSoup** (bs4) and tried some basic scraping.

If you have not yet installed the `Requests <https://requests.readthedocs.io/en/master/>`_ module, do it now (in your virtual environment). ::

    pip install requests

If you have not made a virtual environment yet, see `these instructions <http://bit.ly/install-python3-jupyter>`_.

`The code for this chapter is here. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/scraping>`_

Using ``select()`` instead of ``find()`` or ``find_all()``
----------------------------------------------------------

In `the previous section <scraping.html>`_ we covered several commonly used commands for scraping with BeautifulSoup: ::

    soup.h1.text
    soup.find_all( "td", class_="city" )
    soup.find_all("img")
    soup.find(id="call")

In chapter 12 of `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition), the author covers another command, the ``select()`` method.

This method might hold special appeal to people used to working with JavaScript, because the syntax for targeting HTML elements — inside the parentheses of ``select()`` — follows the same syntax as this commonly used JavaScript method: ::

    document.querySelectorAll()

So instead of ``( "td", class_="city" )``, we would write ``( "td.city" )``, and instead of ``(id="call")``, we would write ``("#call")``.

Note that ``select()`` *always* returns a list, even when only one item is found.

Be mindful that the way you write out what you’re looking for depends on whether you are calling ``select()`` or you are calling ``find()`` or ``find_all()``. You’ll get errors if you mix up the syntax.

Working with lists of Tag objects
---------------------------------

Both ``find_all()`` and ``select()`` always return a Python list. Each item in the list is a BeautifulSoup **Tag object.** You can access any list item using its index — just as you would with any normal Python list.

Try this code in the Python interpreter: ::

    from bs4 import BeautifulSoup
    import requests
    url = "https://weimergeeks.com/examples/scraping/example1.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    images = soup.select('img')
    print(images)

You’ll see that you have a list of IMG elements.

You can call ``.get_text()`` or ``.text`` on a Tag object to get only the text inside the element. To get the text from just one Tag object in a list, use its **list index**: ::

    cities = soup.select('td.city')
    print(cities[0])
    print(cities[0].text)

To get the text from all the items in the list, you need a for-loop: ::

    for city in cities:
        print(city.text)

If an element has **attributes,** you can get a Python **dictionary** containing all of them — again, use an index to see just one item from the list: ::

    images = soup.select('img')
    print( images[0].attrs )

To get a particular attribute for all the IMG elements, you need a for-loop: ::

    for image in images:
        print( image.attrs['src'] )

Another way to get a particular attribute is with ``.get()``: ::

    for image in images:
        print( image.get('src') )

As you see, there are various ways to do the same thing with BeautifulSoup. If you find it confusing, choose one way and stick with it.

When in doubt, refer to the `BeautifulSoup documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ — it’s all on one page, so search it with Command-F.

Finding inside a Tag object
---------------------------

The methods ``find()``, ``find_all()``, and ``select()`` work on Tag objects as well as BeautifulSoup objects (`types of objects are covered here <https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-objects>`_). Here is an example:

.. literalinclude:: ../python_code_examples/scraping/table_scrape.py
   :caption:
   :linenos:

Once we’ve got ``table`` out of ``soup`` (line 9 above), we can go on to find elements inside the Tag object ``table``. First we get a list of all rows (line 12). Then we can loop over the list of row objects (starting on line 15) and make a list of all table cells in each row (line 17). From that list, we can extract the contents of one or more cells. By printing ``cells[1].text`` (line 19), we will see a list of all Scottish monarchs in the first table on the page.

.. note:: Using ``try`` / ``except`` in the script above enables us to skip over the header row of the table, where the HTML tags are ``th`` instead of ``td``.

.
