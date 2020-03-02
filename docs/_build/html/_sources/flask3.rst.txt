Flask Templates
===============

Previous:

1. `Flask intro <flask.html>`_: A very simple Flask app
2. `Flask, part 2 <flask2.html>`_: Values in routes; using an API

Code for this chapter is `here <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask>`_.

In the previous Flask chapters, we wrote some HTML directly into the Flask app script. This is very awkward. Naturally, Flask provides a better way to store the HTML (and CSS) you will want your Flask functions to generate.

Folder structure for a Flask app
--------------------------------

A proper Flask app is going to use multiple files — some of which will be template files. The organization of these files has to follow rules so the app will work. Here is a diagram of the typical structure: ::


    my-flask-app
    ├── static/
    │   └── css/
    │       └── main.css
    ├── templates/
    │   ├── index.html
    │   └── student.html
    ├── data.py
    └── students.py


1. Everything the app needs is in one folder, here named *my-flask-app*.

2. That folder contains two folders, specifically named *static* and *templates*.

   * The *static* folder contains **assets** used by the templates, including CSS files, JavaScript files, and images. In the example, we have only one asset file, *main.css*. Note that it’s inside a *css* folder that’s inside the *static* folder.

   * The *templates* folder contains only templates. These have an ``.html`` extension. As we will see, they contain more than just regular HTML.


3. In addition to the *static* and *templates* folders, this app also contains ``.py`` files. Note that these must be *outside* the two folders named *static* and *templates*.

.. attention:: The templates will not work if this folder structure is not exactly as described above. Your app folder can be named anything (not only *my-flask-app*), but the *static* and *templates* folders must be named and organized as shown above.

Get started with templates
--------------------------

Let’s first imagine a situation where we are going to need a lot of pages that all have the same layout.

For example, we might want to build an app that includes all the U.S. presidents. Each president will have their own page, like this:

.. figure:: _static/images/prespage.png
   :scale: 50 %
   :alt: President page screenshot

We do not want to build 45 pages by hand. We happen to have all the presidential data `in a spreadsheet <https://github.com/macloo/flask-pres-forms-exercise/blob/master/final_app/presidents.csv>`_. Can we make *one HTML template* and be done?

Yes!


Resources
---------

* `Jinja documentation <https://jinja.palletsprojects.com/en/2.11.x/templates/>`_ — All the commands for the Jinja template syntax are here.


.
