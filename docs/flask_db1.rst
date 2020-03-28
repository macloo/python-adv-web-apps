Flask and Databases
===================

To add database functionality to a Flask app, we will use SQLAlchemy.

**SQLAlchemy** is a Python SQL toolkit and object relational mapper (ORM) that enables Python to communicate with the SQL database system you prefer: MySQL, PostgreSQL, SQLite, and others. An ORM converts data between incompatible systems (object structure in Python, table structure in SQL database). SQLAlchemy is basically a **bridge** between Python and a SQL database.

**Flask-SQLAlchemy** is an *extension* for Flask that adds SQLAlchemy to your Flask app.

* `SQLAlchemy documentation <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy documentation <https://flask-sqlalchemy.palletsprojects.com/>`_
* Code for this chapter TK


Setup: Flask-SQLAlchemy
-----------------------

We will install the **Flask-SQLAlchemy** extension to enable us to work with a SQL database in Flask. There are many extensions for Flask; each one adds a different set of functions and capabilities. See the `list of Flask extensions <https://flask.palletsprojects.com/en/1.1.x/extensions/>`_ for more.

In Terminal, change into your Flask projects folder and **activate your virtual environment** there. Then install the extension at the command prompt — where you see ``$`` (Mac) or ``C:\Users\yourname>`` (Windows) — ::

    pip install flask-sqlalchemy

We will use SQLite3 for database examples here. SQLAlchemy can bridge between Python and various different SQL database systems — some of which need an additional module, or library, to be installed. SQLite *does not* require an additional module — the ``sqlite3`` module is included in Python 3.x. `Find other modules for other SQL databases. <https://docs.sqlalchemy.org/en/13/dialects/>`_

.. important:: If you’re using a MySQL or PostgreSQL database, you will need to install a DBAPI module such as ``psycopg2`` (PostgreSQL) or ``PyMySQL`` (MySQL).


Basics of using a database with Flask
-------------------------------------

You’ll *connect* your Flask app to an existing SQL database, whether the app reads from the database, writes to the database, or both. Connecting will require your own database username and database password. (You are the owner of the database.)

.. note:: You *can* create the SQL database using Python, but *that is not required.* If you already have a database, all you need to worry about is how to connect it. If you *do* use Python to create a SQL database (and that’s an “if,” not a necessity), you will only do it once. You don’t create the same database again and again.

Your database may have one table, or more than one table. That depends on what you need, or the structure of the existing SQL database. You’ll need to know the table name(s).

Your app might only *read from* your SQL database. You can write SQL queries to accomplish this — using Flask-SQLAlchemy commands to do so. Note that you won’t write a straightforward SQL query. Here is an example of Flask-SQLAlchemy syntax:

.. code-block:: python

   socks = Sock.query.filter_by(style='knee-high').order_by(Sock.name).all()


The Flask-SQLAlchemy statement to the right of the equals sign, *above,* is equivalent to this standard SQL statement:

.. code-block:: mysql

   SELECT * FROM socks WHERE style="knee-high" ORDER BY name


It is assumed you are familiar with how to write basic SQL queries.


* `Details about writing queries with Flask-SQLAlchemy. <https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records>`_


In addition to *reading from* your SQL database, your Flask app might allow people to *write to* the database. In that case, you will probably want people to log in securely. Alternatively, you might set up a Python script that updates your database on a regular schedule (e.g., writing in new records from a monthly data dump).

You might write a Python script to populate your database from the contents of a CSV file. This would be fairly simple if you only need to run it once. If you need to add records repeatedly (say, once per month) to an existing database, you might need to check whether you are *duplicating records that are already there.* If you need to check for existing records and update them, that’s more challenging.

If people are *writing into* your database, you will want to give them a web form, or forms, for doing so. See `Flask: Web Forms <flask_forms.html>`_ if you need to create a web form in your Flask app.

You will not necessarily need forms if your app only *reads from* the database, but it is possible you’ll want to allow people to search for content, or to choose content from a menu using a ``<select>`` element in a form that queries the database. Then a form or forms will be required.

Of course, you’ll be using templates and all the other aspects of Flask covered in previous chapters here.

For all Python and SQL commands, refer to the links listed under “User’s Guide” in the `Flask-SQLAlchemy documentation <https://flask-sqlalchemy.palletsprojects.com/>`_.


How to connect a MySQL database to a Flask app
----------------------------------------------

Here’s a starter script for testing whether you can connect:




.
