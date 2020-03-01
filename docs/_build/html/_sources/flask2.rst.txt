Flask, Part 2
=============

In the `Flask intro <flask.html>`_, you saw a very simple Flask app in action. Let’s step it up a little.

Code for this chapter is `here <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask>`_.

Your second Flask app
---------------------

The following script demonstrates the use of a *variable* in a Flask **route.** The function can employ the *value* of this variable in many ways. Here, the value will simply appear in the browser window as part of a string.

.. literalinclude:: ../python_code_examples/flask/hello3.py
   :caption:
   :linenos:


We have **two routes** in the script. The first route, for ``'/'``, is not very different from our first Flask app. The second route, for ``'/user/<name>'``, is doing something new.

.. note:: Because of the final two lines in this script, you will run this file in exactly the same way you’ve run every other ``.py`` file in a virtual environment: ::

        python hello3.py

    Do not use ``flask run`` to run this script. That is not necessary, thanks to lines 20 and 21.

When we go to ``localhost:5000`` in the browser, the following code from the Python script creates a functional link in the browser window: ::

    <p><a href="user/Albert">Click me!</a></p>


.. figure:: _static/images/hello3_a.png
   :scale: 50 %
   :alt: The first route in a browser screenshot


When you click the link, the second route in *hello3.py* is called. That is, the relative URL *user/Albert* is sent to the server as an HTTP request. But note — and this is a *key point* — the relative URL in the HTML is ``href="user/Albert"`` and yet the Flask route says: ::

    @app.route('/user/<name>')


.. figure:: _static/images/hello3_b.png
   :scale: 50 %
   :alt: The second route in a browser screenshot

What you should understand about Flask *right now* is that we are able to pass in **changeable values** using the URL.

To test this, **change the text** that comes after ``/user/`` in the browser address bar, and press Enter or Return.

.. figure:: _static/images/hello3_c.png
   :scale: 50 %
   :alt: A variation on the second route in a browser screenshot

Look at the URL in the browser address bar, and look at the text in the browser window.

If you enter the URL *without* a value for ``name`` — e.g. ``localhost:5000/user/`` — you’ll get an HTTP error: “The requested URL was not found on the server.”

Review the route function that makes it happen: ::

    @app.route('/user/<name>')
    def user(name):
        personal = f'<h1>Hello, {name}!</h1>'
        # above - the curly braces {} hold a variable; when this runs,
        # the value will replace the braces and the variable name
        instruc = '<p>Change the name in the <em>browser address bar</em> \
            and reload the page.</p>'
        return personal + instruc


.. note:: Possibly the use of string formatters above is new to you. They are similar to template literals in JavaScript. ::

        personal = f'<h1>Hello, {name}!</h1>'

    The result of that line is equivalent to this string concatenation: ::

        personal = '<h1>Hello, ' + name + '!</h1>'

    `Learn about Python format strings here. <https://realpython.com/python-f-strings/>`_



Putting this to work with an API
--------------------------------

The next script will demonstrate how Flask can be used to send an API request, and then use the response in a formatted string. This is more useful than the previous example script — but **the same idea** of the **variable** in the **route** is used.

In the previous script, we used ``<name>`` in the route and ``name`` in the function to write *Albert* and then *Mindy.* In the **next** script, we will use ``<zip>`` in the route and ``zip`` in the function to submit a U.S. zip code to the OpenWeather API (the **request**). The **response** (in the browser) will tell us the current weather at that location.


The OpenWeather API
+++++++++++++++++++

To use this script for yourself, you will need to get an API key at `OpenWeather <https://openweathermap.org/>`_ (it’s free). Do not allow your API key to be seen by others. I am not sharing my real API key here.

.. note:: See the `configparser chapter <configparser.html>`_ for details about using a ``.cfg`` file to store all your API keys. You don’t need to do this to make the script below work, but make sure you do not *publish* that version with your actual API key in the code, e.g. on GitHub.

`Here is everything you need to know about the OpenWeather API. <https://openweathermap.org/current>`_

We will use the OpenWeather zip code query. A request to an API can be submitted in a web browser. This is the request, or query (not using a real API key): ::

    http://api.openweathermap.org/data/2.5/weather?zip=32611,us&mode=json&units=imperial&appid=12345abcXYZ

In the URL above, you can see I submitted the zip code 32611, JSON as the mode (for the response), and imperial (for temperature in Fahrenheit). The pattern of the URL is shown on the OpenWeather API page.

This is the response from the OpenWeather API, in a browser:

.. figure:: _static/images/weatherres.png
   :scale: 50 %
   :alt: Response from weather API in a browser screenshot

Like most APIs, the OpenWeather API returns a response in a **JSON-formatted string.** (You can opt to get it in other formats.) In the respnse, you can find the *name* (Gainesville), the *temp* (70.05), and the *description* (clear sky). Those **keys** and **values** will be used in the Python script *weather.py* below.


Using Flask to get a response
+++++++++++++++++++++++++++++

After creating a Flask script (*weather.py*) to query the OpenWeather API and write a more readable string into the browser, I ran the script on a February day: ::

    python weather.py

In the browser, I typed three different URLs as shown below.

The zip code 32611 is for Gainesville, Florida.

.. figure:: _static/images/zip1.png
   :scale: 50 %
   :alt: Response from weather API in a browser screenshot

The zip code 10118 is for New York City.

.. figure:: _static/images/zip2.png
  :scale: 50 %
  :alt: Response from weather API in a browser screenshot

The zip code 99508 is for Anchorage, Alaska.

.. figure:: _static/images/zip3.png
 :scale: 50 %
 :alt: Response from weather API in a browser screenshot


The weather script
++++++++++++++++++

.. literalinclude:: ../python_code_examples/flask/weather.py
   :caption:
   :linenos:

*Line 5:* We import the ``requests`` module so that we can use ``request.get()`` to submit the API request (on line 20).

*Line 11:* Provide **the API key** that will be used in code below this line. (Uppercase letters are used for the variable name to denote a constant; see `PEP 8 <https://www.python.org/dev/peps/pep-0008/#constants>`_).

*Line 14:* The API call — the URL for the request. Note how **curly braces** are used at two locations in this string: ``zip={},us`` and ``appid={}``. The curly braces allow a variable or a value to be inserted (on line 20).






.
