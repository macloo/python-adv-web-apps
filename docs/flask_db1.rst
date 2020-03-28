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

In Terminal, change into your Flask projects folder and **activate your virtual environment** there. Then install at the command prompt — where you see ``$`` (Mac) or ``C:\Users\yourname>`` (Windows) — ::

    pip install flask-sqlalchemy

We will use SQLite3 for database examples here. SQLAlchemy can bridge between Python and various different SQL database systems — some of which need an additional module, or library, to be installed. SQLite *does not* require an additional module — the ``sqlite3`` module is included in Python 3.x. `Find other modules for other SQL databases. <https://docs.sqlalchemy.org/en/13/dialects/>`_

.. important:: If you’re using a MySQL or PostgreSQL database, you will need to install a DBAPI module such as ``psycopg2`` (PostgreSQL) or ``PyMySQL`` (MySQL).
