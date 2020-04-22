# note - using a MySQL database here, not SQLite
import pymysql
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app

app.config['SECRET_KEY'] = 'sOmebiGseCretstrIng'

# connect to MySQL database on Reclaim
username = 'my_name'
password = 'my_password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# this is for connection on the server
server  = '127.0.0.1'
# change to YOUR database name, with a slash added as shown
dbname   = '/my_database'
# no socket

# setup required for SQLAlchemy and Bootstrap
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# this database has only ONE table, socks
# identify all of your columns by name and data type as shown
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

# get sock IDs and names for the select menu BELOW
socks = Sock.query.order_by(Sock.name).all()
# create the list of tuples needed for the choices value
pairs_list = []
for sock in socks:
    pairs_list.append( (sock.id, sock.name) )

# Flask-WTF form magic
# set up the quickform - select includes value, option text (value matches db)
# all that is in this form is one select menu and one submit button
class SockSelect(FlaskForm):
    select = SelectField( 'Choose a sock style:',
      choices=pairs_list
      )
    submit = SubmitField('Submit')


# routes

# starting page for app
@app.route('/')
def index():
    # make an instance of the WTF form class we created, above
    form = SockSelect()
    # pass it to the template
    return render_template('index.html', form=form)


# whichever id comes from the form, that one sock will be displayed
@app.route('/sock', methods=['POST'])
def sock_detail():
    sock_id = request.form['select']
    # get all columns for the one sock with the supplied id
    the_sock = Sock.query.filter_by(id=sock_id).first()
    # pass them to the template
    return render_template('sock.html', the_sock=the_sock)


if __name__ == '__main__':
    app.run(debug=True)
