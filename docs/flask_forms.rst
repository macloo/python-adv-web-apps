Flask: Web Forms
================

Previous:

1. `Flask intro <flask.html>`_: A very simple Flask app

2. `Flask, part 2 <flask2.html>`_: Values in routes; using an API

3. `Flask templates <flask3.html>`_: Write HTML templates for a Flask app

4. `Flask: Deploy an app <flask_deploy.html>`_: How to put your finished app online

Code for this chapter is `here <https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask>`_.

In the **Flask Templates** chapter, we built a functioning Flask app. In this chapter, we’ll explore how to add web forms to a similar app.


Introduction
------------

Flask has an extension that makes it easy to create web forms.

WTForms is “a flexible forms validation and rendering library for Python Web development.” With **Flask-WTF,** we get WTForms in Flask.

* WTForms includes security features for submitting form data.
* WTForms has built-in validation techniques.
* WTForms can be combined with Bootstrap to help us make clean-looking, responsive forms for mobile and desktop screens.

`Read the documentation for Flask-WTF. <https://flask-wtf.readthedocs.io/en/stable/>`_


Setup for using forms in Flask
------------------------------

We will install the **Flask-WTF** extension to help us work with forms in Flask. There are many extensions for Flask, and each one adds a different set of functions and capabilities. See the `list of Flask extensions <https://flask.palletsprojects.com/en/1.1.x/extensions/>`_ for more.

In Terminal, change into your Flask projects folder and **activate your virtual environment** there. Then, at the command prompt — where you see ``$`` (Mac) or ``C:\Users\yourname>`` (Windows )— ::

    pip install Flask-WTF

We will also install the **Flask-Bootstrap4** extension to provide Bootstrap styles for our forms. ::

    pip install Flask-Bootstrap4

This installation is done *only once* in any virtualenv. It is assumed you already have Flask installed there.

* `Flask-WTF docs <https://flask-wtf.readthedocs.io/en/stable/>`_
* More details in `WTForms docs <https://wtforms.readthedocs.io/en/stable/>`_
* `Flask-Bootstrap docs <https://pythonhosted.org/Flask-Bootstrap/>`_
* An *alternative* is `Bootstrap Flask <https://bootstrap-flask.readthedocs.io/en/latest/>`_ — but that is NOT used here


Imports for forms with Flask-WTF and Flask-Bootstrap
----------------------------------------------------

You will have a long list of imports at the top of your Flask app file: ::

    from flask import Flask, render_template, redirect, url_for
    from flask_bootstrap import Bootstrap
    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField
    from wtforms.validators import Required

Note as always that Python is case-sensitive, so upper- and lowercase must be used exactly as shown. **The fourth line will change** depending on **your form’s contents.** For example, if you have a SELECT element, you’ll need to import that. `See the complete list <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/forms/WTForms-field-types.csv>`_ of WTForms form field types.

Set up a form in a Flask app
----------------------------

After the imports, these lines follow in the app script: ::


    app = Flask(__name__)

    # Flask-WTF requires an encryption key - the string can be anything
    app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

    # Flask-Bootstrap requires this line
    Bootstrap(app)


Flask allows us to set a “secret key” value. You can grab a string from a site such as `RandomKeygen <https://randomkeygen.com/>`_. This value is used to prevent malicious hijacking of your form from an outside submission.

Flask-WTF's ``FlaskForm`` will automatically create a secure session with CSRF (cross-site request forgery) protection *if this key-value is set.*  **Don’t publish the actual key on GitHub!**

You can read more about ``app.config['SECRET_KEY']`` in this `StackOverflow post <https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key>`_.


Configure the form
++++++++++++++++++

Next, we configure a form that inherits from Flask-WTF’s class ``FlaskForm``. Python style dictates that a **class** starts with an uppercase letter and uses `camelCase <https://www.computerhope.com/jargon/c/camelcase.htm>`_, so here our new class is named ``NameForm`` (we will use the form to search for a name).

In the class, we assign each form control to a unique variable. This form has only one text input field and one submit button.

**Every form control** must be configured here. ::


    class NameForm(FlaskForm):
        name = StringField('Which actor is your favorite?', validators=[Required()])
        submit = SubmitField('Submit')


`Learn more about classes in Python here. <https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes>`_

If you had **more than one form** in the app, you would define more than one new class in this manner.

Note that ``StringField`` and ``SubmitField`` were **imported** at the top of the file. If we needed other form-control types in this form, we would need to import those also. `See a list of all WTForms field types. <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/forms/WTForms-field-types.csv>`_

Note that several field types (such as ``RadioField`` and ``SelectField``) must have an option ``choices=[]`` specified, after the label text. Within the list, each choice is a pair in this format: ``('string1', 'string2')``.

WTForms also has a long list of `validators <https://github.com/macloo/python-adv-web-apps/blob/master/python_code_examples/flask/forms/WTForms-validators.csv>`_ we can use. The ``Required()`` validator prevents the form from being submitted if that field is empty. Note that these validators must also be imported at the top of the file.


Put the form in a route function
++++++++++++++++++++++++++++++++

Now we will use the form in a Flask route: ::


    @app.route('/', methods=['GET', 'POST'])
    def index():
        names = get_names(ACTORS)
        # ACTORS is a list of dictionaries for 100 movie actors, imported with -
        # from data import ACTORS
        form = NameForm()
        # 'form' is the variable name used in this template: index.html
        # NameForm() is the class, explained above
        message = ""
        if form.validate_on_submit():
            name = form.name.data
            # get the text (data) out of the form control with the name "name"
            if name in names:
                # empty the form field
                form.name.data = ""
                id = get_id(ACTORS, name)
                # redirect the browser to another route and template
                return redirect( url_for('actor', id=id) )
            else:
                message = "That actor is not in our database."
        return render_template('index.html', names=names, form=form, message=message)


A crucial line is where we assign our configured form object to a new variable: ::

    form = NameForm()

Be aware that if we had created **more than one** form class, each of those would need to be assigned to a unique variable.


Put the form in a template
++++++++++++++++++++++++++

Before we break all that down and explain it, let’s look at the code in the template *index.html*:
