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













.
