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


How to connect a database to a Flask app
----------------------------------------

Here’s a starter script for testing whether you can connect:

.. literalinclude:: ../python_code_examples/flask/databases/test_local_sqlite_db.py
   :linenos:
   :emphasize-lines: 16
   :caption:

The script above assumes that a SQLite database file (see filename on line 14) is in the same directory as the ``.py`` file. The script will work with any SQLite database file.

Note that line 16 is the key to the connection — it contains the **database connection string,** which will be *different* depending on which SQL database system you are connecting to. The SQLite connection string is simpler than the others, so be sure to read on if you're using MySQL, PostgreSQL, or another system.

Run the script above: ::

    python test_local_sqlite_db.py

Open ``http://localhost:5000/`` in your web browser. If you see the text “It works.” — then all is well. Otherwise, you’ll see an error message that should enable you to resolve the problem.

SQLite resources
++++++++++++++++

SQLite is a SQL database engine that is especially easy to work with because the database — regardless of its size or how many tables it might include — is in a single ``.db`` file.

Unlike other database systems, a SQLite database does not have a username or password option.

* `SQLite homepage <https://www.sqlite.org/index.html>`_
* Download the free `DB Browser for SQLite <https://sqlitebrowser.org/>`_
* SQLite can be used without SQLAlchemy: `Using SQLite3 with Flask <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/>`_

Connecting to a MySQL database
++++++++++++++++++++++++++++++

Two scripts are provided to test a connection to a MySQL database. `They are here. <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/databases/test_mysql_connection>`_ An additional Python module must be installed — PyMySQL — and a username and password **must** be included in the connection string (even an *empty* password has a place).

In addition, when running the MySQL database locally, a socket string must be included. This string will be very different on MacOS and Windows.

The connection string
+++++++++++++++++++++

The database connection string requires a **strict syntax,** or it will not work. The SQLite string is by far the simplest: ::

    'sqlite:///' + db_name

For other database systems, the connection string will be more complex: ::

    'mysql+pymysql://' + username + ':' + password + '@' + server + database

Note, that example is for MySQL only; the protocol will be different for, say, PostgreSQL.


Setting environment variables
+++++++++++++++++++++++++++++

Instead of including username, password, and the whole database connection string *within a Python script,* you can set the complete string as an **environment variable.** Note that the connection string must be complete and correct for your configuration, as discussed in the previous section.

If you set an environment variable for the connection string, then add the following lines near the top of your script: ::

    import os
    # check for environment variable
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")

Eliminate all lines that refer to username, password, server, and database name.

Change the ``app.config`` statement to this: ::

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

Look up how to set an environment variable for your operating system.

.. note::  ``os`` is a built-in Python module.

When setting up a Flask app on a server, there will be an option to set environment variables there. The lines in the Flask script referring to the environment variable will not change.

.. important:: Only one environment variable on your computer, or in an app, can be named ``DATABASE_URL`` — it’s a variable name, so you can change the string to something else, and you can set as many different variables as you need.




.
