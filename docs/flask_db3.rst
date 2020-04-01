Flask: Write to a Database
==========================

In this chapter we focus on writing data to a SQLite database, using Flask-SQLAlchemy.

We will cover:

1. Add a new record: Create a complete new entry and add it to the database.
2. Update a record: Retrieve an existing record and allow the user to edit any part of it, then write the changes to the database.
3. Delete a selected record.

Resources:

* `SQLAlchemy documentation <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy documentation <https://flask-sqlalchemy.palletsprojects.com/>`_
* `Code for this chapter <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/databases/flask_db_write>`_

The database
------------

We will use the same SQLite database from the chapter `Flask: Read from a Database <flask_db2.html>`_.

The database is named *sockmarket.db.* It has only one table, named **socks.** It has seven fields: *id, name, style, color, quantity, price,* and *updated.* You will see the table name and the field names later, in the Python code. The image below is a screenshot from the `DB Browser for SQLite <https://sqlitebrowser.org/>`_, showing the top rows of the **socks** table.

.. figure:: _static/images/socks_db_browser.png
   :alt: Socks table in DB Browser screenshot

It is essential to get your **database connection** working without errors before you try to do more with the database and Flask.

* Refer to `Flask and Databases <flask_db1.html>`_ to test your database connection.
