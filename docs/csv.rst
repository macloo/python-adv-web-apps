CSV Files
=========

This section is based in part on chapter 16 in Sweigart’s `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (second edition).

- `Python scripts for this section <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/csvs>`_

- `Python documentation for dictionaries <https://docs.python.org/3/library/csv.html>`_

Introduction to CSV files
-------------------------

CSV stands for comma-separated values. A CSV file can be opened in Google Sheets or Excel and will be formatted as a spreadsheet. However, a CSV file is actually a plain-text file. It can also be opened with a text editor program such as Atom.

CSVs give us a good, simple way to organize data without using a database program. It's easy to read from and write to CSV files with Python.

The csv module in Python
------------------------

This is a built-in module, so you do not need to install it, However, you must import it in any script that uses it. ::

    import csv

After the import, you can use the methods that are part of the module: ::

    csv.reader()
    csv.writer()
    csv.DictReader()
    csv.DictWriter()

Note that using methods from the ``csv`` module will also involve use of Python's file handling functions, such as ``.open()``. These are covered in `Reading and Writing Files <working_with_files.html>`_ here.

Writing to a CSV
----------------
