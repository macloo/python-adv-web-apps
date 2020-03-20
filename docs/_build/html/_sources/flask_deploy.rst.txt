Flask: Deploy an App
====================

Previous:

1. `Flask intro <flask.html>`_: A very simple Flask app

2. `Flask, part 2 <flask2.html>`_: Values in routes; using an API

3. `Flask templates <flask3.html>`_: Write HTML templates for a Flask app

Code for this chapter is `here <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask>`_.

In the Flask Templates chapter, we built a functioning Flask app. In this chapter, we’ll explore several ways to pt that Flask app online.

Introduction
------------

When professionals deploy their Python web apps, nowadays they commonly deploy to a cloud service such as `Amazon’s AWS <https://aws.amazon.com/>`_, `Heroku <https://www.heroku.com/>`_, or `Google App Engine <https://cloud.google.com/free/>`_.

One thing to understand, though, is that often they do not deploy a Python executable. That is, the site they upload to a web server is not the Flask app and its associated templates, etc., but rather a traditional website with hard-coded HTML files that has been *“baked out”* from Flask.

In this document, we’ll learn how to do that. Then we will also learn how to install a Flask app (one that has not been “baked out”) on:

* A typical web hosting service such as Reclaim Hosting `<https://reclaimhosting.com/>`_, using a simple **cPanel** service there.

* Heroku, via ``git`` commands, and using the Gunicorn server.

“Baking it out” with Frozen-Flask
---------------------------------

**Frozen-Flask** is a Flask extension, so we’ll need to install it. In Terminal, change into your Flask projects folder and **activate your virtual environment** there. Then install at the command prompt (``$`` or ``C:\Users\yourname>``): ::

    pip install Frozen-Flask

After installing the extension, create **a new file** inside the folder containing only the Flask app you want to “freeze.” Name the new file *freeze.py* and copy/paste this script into it:

.. literalinclude:: ../python_code_examples/flask/freeze.py
   :caption:

Save all your open files.

If the Flask web server is running, quit it with Control-C.

In Terminal, in the directory containing the Flask app, enter this at the command prompt: ::

    python freeze.py

**If freezing worked:** Inside your Flask app folder, you’ll now see a new folder named *build*. Open it. Inside *build*, you’ll see all the files created by Frozen-Flask.

.. figure:: _static/images/freezer.png
   :scale: 50 %
   :alt: Flask app folder with build screenshot

The entire *build* folder can be uploaded to a web server, and the folder name can be changed (from *build* to anything) — and all the pages will work. (Just don't change or rename anything inside the *build* folder.)

Need to update the site? Make your edits, run *freeze.py* again, and re-deploy.

Benefits of freezing
++++++++++++++++++++

Pause for a moment and consider this: Imagine you needed to build a site with detailed data about the 535 members of the U.S. Congress. You build it with Flask (using a CSV file, a Python dictionary, or an SQL database to generate all the data) with two or maybe three HTML templates. Then you run *freeze.py* and in seconds you have 535 individual files, which you just upload as one folder, and you’re done.

Similar apps might produce pages for:

* 190 pages for each dog breed in the American Kennel Club
* 318 pages for each character in all the Harry Potter novels
* 3,144 counties and county equivalents in the United States
* 6,909 living languages in the world

When there are changes to the data, you update the data source, re-freeze and re-deploy.

Freezer errors
++++++++++++++

**If freezing did not work:** This may happen because your app uses dynamic routes similar to this: ::

    @app.route('/actor/<id>')

You might need to add a `URL generator <https://pythonhosted.org/Frozen-Flask/#url-generators>`_ to the *freeze.py* file.

For example: ::

    from data import ACTORS

    @freezer.register_generator
    def actor():
        for item in ACTORS:
            yield { 'id': item['id'] }

You can definitely freeze an app with dynamic route information, but you might need to play around with it a bit before you get it working.

Some apps *cannot* work via freezing. See below for details.

Read the `full documentation <http://pythonhosted.org/Frozen-Flask/>`_ for Frozen-Flask.
