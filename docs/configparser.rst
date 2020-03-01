configparser
============

Python’s build-in module ``configparser`` provides a handy way to manage API keys that you always want to keep out of any public code in GitHub repos, gists, etc.

This chapter shows a quick, easy way for beginners to use a ``.cfg`` file to keep secret keys and tokens in one place.


Set up your config file
-----------------------

Let’s say all your Python work and project folders are inside a folder named ``python`` on your computer. We are looking at files you run locally, not on a server.

1. To make your config file easy to access, but not likely to be deleted (by you) by accident, **create** a new folder in that top-level folder — which I will assume is named ``python`` — on your computer.

2. Name the new folder ``config``.

3. Inside the ``config`` folder, **create** a new file named ``keys_config.cfg``. This is a plain-text file. You can create it in Atom or any code editor.

4. Write at least one key — or set of keys and tokens — into the file in the exact pattern shown below. Then save the file. ::

    [openweather]
    api_key = mt732wbt5kh5ea4bkw7qytbb9gdkaew4

    [twitter]
    consumer_key = d53Qe4uf5LMWuQeQFFG66n6BN
    consumer_secret = Yxf5n2BwnRELRrkkVjWgpTu48sz5KwGD52324PuwkFWdmVGP4m
    access_token = 9922431-d53Qe4uf5LMWuQeQFFG66n6BN
    access_token_secret = ubfWMR8WYucrzeaQdrqkm6SrhYTMVQSsxZWpNbtUCMX5u

    [google]
    api_key = ubfWMR8WYucrzeaQdrqkm6SrhYTMVQSsxZWpNbtUCMX5u


These are not real keys. Do not use them.

Note, there are no quotation marks in the file.

The name of the vendor or source is in brackets.

Use linespaces between items exactly as shown.


Accessing the config file
-------------------------

Your config file can contain keys and tokens for many different APIs. When you are writing a Python script to access a particular API, you will want to get the keys only for that *one* API.

For an example, let’s say you’re accessing the `OpenWeather <https://openweathermap.org/>`_ API in a new Python script. Your script is in a folder named ``weather``, and that folder is inside the ``python`` folder referred to above. In that case, the code in your script is: ::

    from configparser import ConfigParser
    config = ConfigParser()
    config.read('../config/keys_config.cfg')

    API_KEY = config.get('openweather', 'api_key')

Note, you will need to ensure that the **path** on the third line above matches your system.

You will use ``config.get()`` separately for each key or token.

.
