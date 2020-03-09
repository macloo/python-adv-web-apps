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

.. attention:: The templates will not work if this folder structure is not exactly as described above. Your app folder can be named anything (not only *my-flask-app*), but the *static* and *templates* folders must be named and organized as shown above. The *static* folder can contain multiple folders and files.

Get started with templates
--------------------------

Let’s first imagine a situation where we are going to need a lot of pages that all have the same layout.

For example, we might want to build an app that includes all the U.S. presidents. Each president will have their own page, like this:

.. figure:: _static/images/prespage.png
   :scale: 50 %
   :alt: President page screenshot

We do not want to build 45 pages by hand. We happen to have all the presidential data `in a spreadsheet <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/presidents/presidents.csv>`_. Can we make *one HTML template* and be done?

Yes!

Here is an excerpt from that template: ::

    <h1>{{ pres['President'] }}</h1>

    <p>{{ pres['President'] }}, the {{ ord }} president of the
       United States, was born on {{ pres['Birth-date'] }}, in
       {{ pres['Birthplace'] }}. He was {{ pres['Age-when-took-office'] }}
       when he took office on {{ pres['Took-office'] }}. Member:
       {{ pres['Party'] }} Party.</p>

That might look slightly intimidating, but notice that inside each double-pair of curly braces is a **key** (in square brackets) that tells you exactly which information item will appear there. So, for Lincoln:

   *Abraham Lincoln, the 16th president of the United States, was born on 2/12/1809, in LaRue County, Kentucky. He was 52 when he took office on 3/4/1861. Member: Republican/National Union Party.*

How does a Flask app use a template?
++++++++++++++++++++++++++++++++++++

In the previous chapter, `Flask, part 2 <flask2.html>`_, you saw this route function: ::

    @app.route('/user/<name>')
    def user(name):
        personal = f'<h1>Hello, {name}!</h1>'
        instruc = '<p>Change the name in the <em>browser address bar</em> \
            and reload the page.</p>'
        return personal + instruc

Let’s transform that so it uses a template.

1. Put the HTML into a template: ::

    <h1>Hello, {{ name }}!</h1>

    <p>Change the name in the <em>browser address bar</em>
        and reload the page.</p>

2. Save the template file as *hello.html* in the *templates* folder.

3. Edit the route function. Remove the HTML. Change the return statement — call the ``render_template`` function. That is how we get the template! ::

    @app.route('/user/<name>')
    def user(name):
        return render_template('hello.html', name=name)

4. We must import the ``render_template`` module, so add it to the line at the top of the Flask app script: ::

    from flask import Flask, render_template


.. note:: The template needs to be a complete HTML file, with all the usual elements such as HTML, HEAD, and BODY. See the complete example below.


.. literalinclude:: ../python_code_examples/flask/first_template_ex/templates/hello.html
   :caption:
   :language: html


.. attention:: In the HEAD above, in the LINK element, note the syntax for linking to a file in the *static* folder. The CSS file is just a normal CSS file, but it must be in the *static* folder for the Flask app.

Syntax for a path to a file in the *static* folder: ::

    href="{{ url_for('static', filename='main.css') }}"

Syntax for a path to a file inside a folder in the *static* folder: ::

    scr="{{ url_for('static', filename='images/foo.jpg') }}"


☞ `View the live “hello” app here. <https://first-baby-flask-app.herokuapp.com/>`_

☞ `All the “hello” app’s files are here. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/first_template_ex>`_



How are variables passed from app to template?
++++++++++++++++++++++++++++++++++++++++++++++

The templates in Flask are handled by the Jinja template engine, which comes with Flask when you first install it.

The ``render_template()`` function both selects the template file to be used and passes to it any values or variable it needs. ::

    return render_template('example.html',
        name=name, phone=phone_number, state='FL')

We can pass as many variables as necessary to the template. In the example above, the **template** must contain variables for *name, phone,* and *state.* That is, these expressions must be somewhere in the template named *example.html*: ::

    {{ name }}
    {{ phone }}
    {{ state }}

The *value* (on the right side of the equals sign) must come from the code in the Flask app file. In the example above, both *name* and *phone_number* must already have a value before the ``return render_template()`` line. Note that ``'FL'`` is a string — we can pass in a string, integer, float, or Boolean.

It’s also possible to pass lists or dictionaries as *values* to a template. Here’s a line from `the presidents app <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/presidents>`_: ::

    return render_template('president.html',
        pres=pres_dict, ord=ord, the_title=pres_dict['President'])

The template file is named *president.html,* and the values depend on a Python dictionary, ``pres_dict``, that was defined earlier in the Flask app script. We can see the following expressions in the template’s HTML: ::

    {{ ord }}
    {{ pres['President'] }}
    {{ pres['Birth-date'] }}
    {{ pres['Birthplace'] }}

Why ``pres`` and not ``pres_dict``? Because ``pres=pres_dict``. In the ``render_template()`` function call, the dictionary ``pres_dict`` is assigned to the template’s variable ``pres``.

If you need help understanding Python dictionaries, see the `Dictionaries chapter <dicts.html>`_.

In another template, *base.html,* we can see this expression in the HEAD element: ::

    <title>{{ the_title }}</title>

Because ``the_title=pres_dict['President']``, the HTML TITLE element will be filled in with the value of the dictionary item that has the **key** ``'President'``.

.. figure:: _static/images/prestitle.png
   :scale: 50 %
   :alt: President title screenshot

Recall that the HTML TITLE is visible in the browser tab, as seen above.

.. attention:: If a template uses a lot of variables, it’s *much* shorter and easier to pass a dictionary to the template than to specify all the individual variables in the ``render_template()`` function.



Walkthrough of the presidents app
---------------------------------

Now we will examine this app so you can build one like it yourself.

☞ `View the live presents app here. <https://weimergeeks.com/flask_pres/>`_

☞ `View the code for the presidents app. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/presidents>`_

Converting a CSV to a list of dictionaries
++++++++++++++++++++++++++++++++++++++++++

This is covered in `the CSVs chapter <csv.html#reading-into-a-dictionary>`_. All the data we need about the U.S. presidents is in this `CSV file <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/presidents/presidents.csv>`_.

Early in the Flask app in *presidents.py,* we create a **list** of dictionaries named ``presidents_list``. Each **item** in the list is a dictionary. Each dictionary contains all the data about ONE president. That is, each dictionary is equivalent to one row from the original CSV.

We can use ``presidents_list`` to:

1. Populate a template with all the data about a selected president.
2. Use a unique ID number — in the **key** ``'Presidency'`` — to determine which president has been selected. This will be used in the Flask **route**: ::

    @app.route('/president/<num>')

3. Create a list of pairs in which each pair consists of the unique ID and the name of the president it belongs to. This will be used to create an HTML list of all the presidents’ names, which are links to the Flask route.

Here is the top of the *presidents.py* script:

.. literalinclude:: ../python_code_examples/flask/presidents/presidents.py
   :lines: 1-8
   :linenos:

The list is created on line 8, using a function in an external file named *modules.py*. The function ``convert_to_dict()`` was imported from that file on line 2.







Resources
---------

* `Jinja documentation <https://jinja.palletsprojects.com/en/2.11.x/templates/>`_ — All the commands for the Jinja template syntax are here.

* `Flask documentation <https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates>`_ for ``render_template()``.

.
