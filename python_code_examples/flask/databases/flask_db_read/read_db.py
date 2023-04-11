""" read from a SQLite database and return data to templates """

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os.path
from flask_bootstrap import Bootstrap5

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'sockmarket.db'
# note - path is necessary for a SQLite db!!!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)

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

#routes

@app.route('/')
def index():
    # get a list of unique values in the style column
    styles = db.session.execute(db.select(Sock)
        .with_only_columns(Sock.style).distinct())
    return render_template('index.html', styles=styles)


@app.route('/inventory/<style>')
def inventory(style):
    try:
        socks = db.session.execute(db.select(Sock)
            .filter_by(style=style)
            .order_by(Sock.name)).scalars()
        return render_template('list.html', socks=socks, style=style)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
