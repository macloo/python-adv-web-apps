""" write to a SQLite database with forms, templates """

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'

# Flask-Bootstrap requires this line
Bootstrap(app)

# the name of the database; add path if necessary
db_name = 'sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

    def __init__(self, name, style, color, quantity, price, updated):
        self.name = name
        self.style = style
        self.color = color
        self.quantity = quantity
        self.price = price
        self.updated = updated

# forms with Flask-WTF

# form for add_record and update_record
# each field includes validation requirements and messages
class AddRecord(FlaskForm):
    # id used by update_record
    id_field = HiddenField()
    name = StringField('Sock name', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=3, max=25, message="Invalid sock name length")
        ])
    style = SelectField('Choose the sock style', [ InputRequired()],
        choices=[ ('', ''), ('ankle', 'Ankle'),
        ('knee-high', 'Knee-high'),
        ('mini', 'Mini'),
        ('other', 'Other') ])
    color = StringField('Color', [ InputRequired(),
        Regexp(r'^[A-Za-z\s\-\'\/]+$', message="Invalid color"),
        Length(min=3, max=25, message="Invalid color length")
        ])
    quantity = IntegerField('Quantity in stock', [ InputRequired(),
        NumberRange(min=1, max=999, message="Invalid range")
        ])
    price = FloatField('Retail price per pair', [ InputRequired(),
        NumberRange(min=1.00, max=99.99, message="Invalid range")
        ])
    # updated date - handled in the route
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

# +++++++++++++++++++++++
# get local date - does not account for time zone
# note: date was imported at top of script
def stringdate():
    today = date.today()
    date_list = str(today).split('-')
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string

# +++++++++++++++++++++++
# routes

@app.route('/')
def index():
    # get a list of unique values in the style column
    styles = Sock.query.with_entities(Sock.style).distinct()
    return render_template('index.html', styles=styles)

@app.route('/inventory/<style>')
def inventory(style):
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    return render_template('list.html', socks=socks, style=style)

# add a new sock to the database
@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form1 = AddRecord()
    if form1.validate_on_submit():
        name = request.form['name']
        style = request.form['style']
        color = request.form['color']
        quantity = request.form['quantity']
        price = request.form['price']
        # get today's date from function, above all the routes
        updated = stringdate()
        # the data to be inserted into Sock model - the table, socks
        record = Sock(name, style, color, quantity, price, updated)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for sock {name} has been submitted."
        return render_template('add_record.html', message=message)
    else:
        # show validaton errors
        flash('placeholder')
        return render_template('add_record.html', form1=form1)


# error handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500


if __name__ == '__main__':
    app.run(debug=True)
