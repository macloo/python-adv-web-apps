Flask: Read from a Database
===========================

It is essential to get your **database connection** working without errors before you try to do more with the database and Flask.

* Refer to `the previous chapter <flask_db1.html>`_ to test your database connection.

In this chapter we focus on reading data from a SQLite database, using Flask-SQLAlchemy.

* `SQLAlchemy documentation <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy documentation <https://flask-sqlalchemy.palletsprojects.com/>`_
* `Code for this chapter <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/databases>`_

The database
------------

The SQLite database used here is named *sockmarket.db.* It has only one table, named **socks.** It has seven fields: *id, name, style, color, quantity, price,* and *updated.* You will see the table name and the field names later, in the Python code. The image below is a screenshot from the `DB Browser for SQLite <https://sqlitebrowser.org/>`_, showing the top rows of the **socks** table.

.. figure:: _static/images/socks_db_browser.png
   :alt: Socks table in DB Browser screenshot


First read
----------

Without templates or anything fancy, let’s attempt to read some data from the database and return it in the browser.

.. literalinclude:: ../python_code_examples/flask/databases/read_db_basic.py
   :linenos:
   :lines: 1-31
   :caption:

Everything up to line 18 comes from the script explained `in the previous chapter <flask_db1.html#how-to-connect-a-database-to-a-flask-app>`_.

Lines 21–29 provide a *model* so that Python can translate the **socks** table. It’s a Python class that inherits from the ``Model`` class from SQLAlchemy. (Remember, ``db`` refers to SQLAlchemy.) We could name the new class anything, but ``Sock`` makes sense because this table’s data as all about socks.

If your database has *more than one table,* you will need to create an additional class like this for each additional table. Note:

* Identify the primary_key field as shown (line 23).
* Write the field names *exactly* as they appear in the table.
* In ``__tablename__ = 'socks'``, note that the name of the table is case-sensitive. Match it to your actual table’s name.
* ``String``, ``Integer`` or ``Float`` must match the data type in your fields.
* Include *every* field in the table.

`See all possible data types here. <https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example>`_

We will provide only one route to start with, and it includes a try/except just like the example `in the previous chapter <flask_db1.html#how-to-connect-a-database-to-a-flask-app>`_.


.. literalinclude:: ../python_code_examples/flask/databases/read_db_basic.py
   :linenos:
   :lines: 31-49
   :lineno-start: 31
   :emphasize-lines: 6
   :caption:


The only code that talks to the database is in line 36.

1. ``socks`` is a new variable. We assign to it the data we are pulling from the database.
2. ``Sock.query`` refers to the class we built, Sock, starting on line 21. We are querying the table specified in that class.
3. ``.filter_by()`` limits what we’re asking for. It’s the ``WHERE`` clause in regular SQL.
4. ``style='mini'`` — ``style`` is a field name in this table. ``'mini'`` is a value in that field (column). So we will get only socks with the style “mini” — not “knee-high,” “ankle,” or “other.”
5. ``order_by()`` selects a field (column) to determine the *order* of the results listing. This is optional. Any field could be used.
6. ``Sock.name`` refers to the property ``name`` in the Sock class.
7. ``.all()`` is tacked onto the end of every query, unless you expect or want only one record to be returned — in which case, use ``.first()`` instead.

Lines 37–40 create a string using the data in ``socks`` and adding HTML tags around th data — ``<ul>`` and ``<li>`` tags should be familiar to you.

After the for-loop completes, and the final closing tag ``</ul>`` is concatenated to the string, the value of ``sock_text`` will be:

.. code-block:: html

    <ul><li>D'Shawn, blue</li><li>Divine, white stripes on navy</li><li>Faye, dark purple</li>
    <li>Isabel, white</li><li>Jenny, blue</li><li>Jo-Anne, brown</li><li>Krissie, blue</li>
    <li>Lizzy, red</li><li>Nancie, purple</li><li>Tanya, red</li><li>Terrie, blue stripe</li></ul>

Assuming everything worked, that is what will be **returned** (line 41).

The rest of the code (lines 42–49) is from `the database intro chapter <flask_db1.html#how-to-connect-a-database-to-a-flask-app>`_.

When the code runs, this is the result in the browser:

.. figure:: _static/images/db_read_result.png
   :scale: 50 %
   :alt: Results in browser screenshot

We have successfully queried data from this database and used it in a Flask route. Now we will put it into a Flask template.




.
