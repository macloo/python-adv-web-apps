Flask and Databases with SQLAlchemy
===================================

**SQLAlchemy** is a Python SQL toolkit and object relational mapper (ORM) that enables Python to communicate with the SQL database system you prefer: MySQL, PostgreSQL, SQLite. An ORM converts data between incompatible systems (object structure in Python, table structure in SQL database). SQLAlchemy is basically a **bridge** between Python and a SQL database.

**Flask-SQLAlchemy** is an *extension* for Flask that adds SQLAlchemy to your Flask app.

* `SQLAlchemy documentation <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy documentation <https://flask-sqlalchemy.palletsprojects.com/>`_
* Code for this chapter TK


Setup for using Flask-SQLAlchemy
--------------------------------

We will install the **Flask-SQLAlchemy** extension to enable us to work with a SQL database in Flask. There are many extensions for Flask; each one adds a different set of functions and capabilities. See the `list of Flask extensions <https://flask.palletsprojects.com/en/1.1.x/extensions/>`_ for more.

In Terminal, change into your Flask projects folder and **activate your virtual environment** there. Then install at the command prompt — where you see ``$`` (Mac) or ``C:\Users\yourname>`` (Windows) — ::

    pip install flask-sqlalchemy

xxx
