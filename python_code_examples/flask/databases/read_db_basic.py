""" read from a SQLite database and return data """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


# each table in the database needs a class to be created for it
# this class is named Sock because the database contains info about socks
# and the table in the database is named: socks
# db.Model is required - don't change it
# identify all columns by name and their data type
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

#routes

@app.route('/')
def index():
    try:
        socks = Sock.query.filter_by(style='mini').order_by(Sock.name).all()
        sock_text = '<ul>'
        for sock in socks:
            sock_text += '<li>' + sock.name + ', ' + sock.color + '</li>'
        sock_text += '</ul>'
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)
