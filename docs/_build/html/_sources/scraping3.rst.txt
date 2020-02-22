Web Scraping, Part 3
====================

In the previous two scraping chapters here, you downloaded and installed both **BeautifulSoup** and **Requests** in a Python virtual environment. (We will continue in the same environment.) You also learned the basics of scraping with BeautifulSoup.

In this chapter, more advanced topics are covered.

`The code for this chapter is here. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/scraping>`_

Using Selenium
--------------

We can use `Selenium <https://selenium.dev/>`_ together with BeautifulSoup when BeautifulSoup *alone* is unable to get the contents we want from a web page. **Two common situations where this comes up:**

1. JavaScript is writing the contents into the page after it opens; and/or
2. Contents are not available until you click a button, fill a form, open a menu, etc.

The documentation for setting up Selenium is not easy to use, so **follow this step-by-step guide**:

`Getting started with Selenium <http://bit.ly/selenium-intro>`_

You will need to install Selenium and also a **driver** for the web browser you want to use (Chrome or Firefox). This is all covered in the “Getting Started” doc. Make sure to do the Selenium install with your virtual environment activated.

When you examine the test scripts (linked in the “Getting Started” doc and also found in this repo), notice that after doing the ``driver`` stuff, **this line** creates a ``page`` variable just like we have been doing all along with our BeautifulSoup scrapers: ::

    page = driver.page_source

.. attention:: Once you have that ``page`` variable, you can proceed as usual with a ``soup`` variable and BeautifulSoup scraping. You DO NOT need to use ``driver`` and a new set of selectors as shown in the Selenium documentation and many tutorials.

Selenium commands
+++++++++++++++++

**To manipulate elements on the page** with Selenium, you *will* need to use Selenium commands such as ``.find_element_by_css_selector()`` — as seen in the example below.

.. literalinclude:: ../python_code_examples/scraping/selenium_test3.py
   :caption:

The page being scraped shows only 32 movies until you click a button at the bottom. Each time you click the bottom button, more movies are visible on the original page. By having Selenium click the button eight times, we are able to scrape information for 275 movies instead of only 32.

If you run the code above, be sure you have installed both BeautifulSoup and Selenium. The ``time`` and ``random`` modules are built-ins, so you do not need to install those beforehand.

Other Selenium methods for locating HTML elements are listed `here <https://selenium-python.readthedocs.io/locating-elements.html>`_.

Headless Selenium
+++++++++++++++++

In normal use, Selenium launches a web browser, and you can see it on your screen. You will see the page scrolling and so on as if an invisible person were controlling the browser.

Alternatively, it is possible to use **headless mode** instead of a physical browser with Selenium. This is NOT covered in the “Getting Started” doc.

`Code for using Chrome in headless mode. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/scraping/headless_selenium.py>`_

More advanced Selenium techniques
+++++++++++++++++++++++++++++++++

If you’re still having trouble scraping a page even after adding Selenium to your Python script, the culprit might be a timing issue. See the `Selenium documentation <https://selenium-python.readthedocs.io/waits.html>`_ for an explanation of an *implicit wait* and the use of ``expected_conditions``, a Selenium module.

Look at how the page behaves when you access it normally, yourself, to determine whether to add this kind of code to your script.

Also see the next section below.

Timing matters
--------------

This one line tells your Python script to pause for 3 seconds: ::

    time.sleep(3)

Before using ``time.sleep()``, you must import Python’s ``time`` module. See `the Python docs <https://docs.python.org/3/library/time.html#time.sleep>`_.

You will need to think carefully about the best place to insert this line in your code. You are not likely to need it when you are *initially* testing your code, line by line, to write a scraper script, but once you are ready to run the completed script on *dozens* or *hundreds* of web pages, then you must add some sleep time.

.. note:: It’s very bad to overload or overwork a website by making a scraper that runs too fast. It’s also likely that the server will block your IP address if you do this! By inserting ``time.sleep()``, you can build in pauses that make your code less rude.

Using a different parser
------------------------

Sometimes you can’t get BeautifulSoup Tag objects out of a web page because the HTML is poorly formatted. In that case, it can help to use a different **parser.** Instead of: ::

    soup = BeautifulSoup(page, 'html.parser')

You can write: ::

    soup = BeautifulSoup(page, 'html5lib')

Before you can use the ``html5lib`` parser, however, you must install it with your *virtual environment* activated: ::

    pip install html5lib

Another parser option is ``lxml``. You can read about the differences among Python parsers:

- `Stack Overflow post <https://stackoverflow.com/questions/45494505/python-difference-between-lxml-and-html-parser-and-html5lib-with-beautifu>`_

- BeautifulSoup docs: `Differences between parsers <https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers>`_

**tl;dr** — Sometimes one parser just works better than another. **lxml** is a much faster parser than **html5lib**, so if you are churning through a gazillion pages, that might make **lxml** a better choice. **html5lib** is better at reading badly formatted HTML, however.

Sending HTTP headers in your script
-----------------------------------

Sometimes a website blocks your attempts to scrape because your code (without using Selenium) lacks the headers that a real web browser would send with an HTTP request.

This doesn’t (always) mean you have to use Selenium. Instead, you can send a proper set of headers as part of a regular script with BeautifulSoup and Requests.

Use `WhatIsMyBrowser.com <https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending>`_ to find your web browser’s **user agent** and other values.

The example code below comes from a time when I needed to use headers in a scraping script that downloaded messages from a large online forum. The site completely shut out my script until I added a full set of header data: ::

    hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

After that, I used the variable ``hdr`` to get the page and then create my ``soup``: ::

    page = requests.get(url, headers=hdr)
    soup = BeautifulSoup(page.text, 'html5lib')

Notice that I replaced the usual ``'html.parser'`` with ``'html5lib'``. See  “Using a different parser,” above.

**I did not need to use Selenium at all to scrape that forum site.** The headers got me in, and everything after that was normal BeautifulSoup stuff.

.. tip:: You can see the actual headers *your* web browser is sending if you go to `this page <https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending>`_. Do not copy my example code, as it is probably outdated now.


Using chunks and ``iter_content()``
-----------------------------------

In chapter 12 of `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition), Sweigart provides a script to scrape the XKCD comics website (“Project: Downloading All XKCD Comics”). The code in step 4, which is part of a longer while-loop, uses the **Requests** method ``iter_content()``: ::

    res = requests.get(comicUrl)
    # ... other code
    # imageFile was previously opened
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

.. note:: The `Requests <https://requests.readthedocs.io/en/master/>`_ library is used here. To use ``iter_content()``, the ``requests`` module must be imported.

The first thing to understand is **in what cases** chunking would be needed. Reading a regular web page into memory (for scraping with BeautifulSoup) *does not* call for chunking. We need chunking for **binary files** that we are **saving to disk.** Examples would be large image files, or — very common for journalists who are scraping — **PDF files.**

In the code above, the variable ``comicUrl`` points to the location of one image file. It is assigned to a Response object with the variable name ``res``. You can only use ``iter_content()`` on a Response object.

Downloading the binary data of the file in chunks that are *smaller than the complete file* is basically a way to make sure you actually get the files without overloading your local memory. You not only download it in chunks; you also *write it to your local hard drive* in chunks.

The value in parentheses above — ``100000`` — means each chunk is 100,000 bytes *or smaller.*

From the `Requests documentation <https://requests.readthedocs.io/en/master/user/advanced/#chunk-encoded-requests>`_: “In an ideal situation you’ll have set ``stream=True`` on the request, in which case you can iterate chunk-by-chunk by calling ``iter_content`` with a ``chunk_size`` parameter of ``None``. If you want to set a maximum size of the chunk, you can set a ``chunk_size`` parameter to any integer.”

Here is an generic example of chunking code from `a blog post <http://masnun.com/2016/09/18/python-using-the-requests-module-to-download-large-files-efficiently.html>`_: ::

    response = requests.get(url, stream=True)
    handle = open(target_path, 'wb')
    for chunk in response.iter_content(chunk_size=512):
        if chunk:   # filter out keep-alive new chunks
            handle.write(chunk)
    handle.close()

Note that ``stream=True`` is used in the GET Request.


When all else fails
-------------------

Sometimes a website might block all your attempts to scrape it. Before you give up, I recommend you consult this book, especially chapter 14 and “The Human Checklist” at the end of that chapter:

*Web Scraping with Python: Collecting More Data from the Modern Web* (2nd edition), by Ryan Mitchell, 2018 (`link <http://shop.oreilly.com/product/0636920078067.do>`_).

It’s not particularly beginner-friendly, but at some point you’ll advance beyond the beginner level, and then you should invest in this resource.
