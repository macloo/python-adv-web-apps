""" using a MySQL database here, not SQLite """
import pymysql
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SelectField, SubmitField
from flask_bootstrap import Bootstrap5

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)

# make sure the database username, database password and
# database name are correct
username = 'my_name'
password = 'my_password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# this is for connection on the server
server  = '127.0.0.1'
# change to YOUR database name, with a slash added as shown
dbname   = '/my_database'
# there is no socket

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'sOmebiGseCretstrIng'
# initialize the app with Flask-SQLAlchemy
db.init_app(app)

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

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


# get ID-name pairs to use in a select menu
# the socks query below does not work without app_context()
# see https://flask.palletsprojects.com/en/2.2.x/appcontext/
with app.app_context():
    # get sock IDs and names for the select menu BELOW
    socks = db.session.execute(db.select(Sock)
        .order_by(Sock.name)).scalars()
    # create the list of tuples needed for the choices value
    pairs_list = []
    for sock in socks:
        pairs_list.append( (sock.id, sock.name) )


# Flask-WTF form magic
# set up the select drop-down with IDs as values and sock names as
# the menu options - using pairs_list created above
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
    the_sock = db.get_or_404(Sock, sock_id)
    # pass it to the template
    return render_template('sock.html', the_sock=the_sock)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
