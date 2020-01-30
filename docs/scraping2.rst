Web Scraping, Part 2
====================

You have installed **BeautifulSoup** (bs4) and tried some basic scraping.

If you have not yet installed the `Requests <https://requests.readthedocs.io/en/master/>`_ module, do it now (in your virtual environment). ::

    pip install requests

If you have not made a virtual environment yet, see `these instructions <http://bit.ly/install-python3-jupyter>`_.

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
