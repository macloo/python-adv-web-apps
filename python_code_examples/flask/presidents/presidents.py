from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts
presidents_list = convert_to_dict("presidents.csv")

# first route

@app.route('/')
def index():
    ids_list = []
    name_list = []
    # fill one list with the number of each presidency and
    # fill the other with the name of each president
    for president in presidents_list:
        ids_list.append(president['Presidency'])
        name_list.append(president['President'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")

# second route

@app.route('/president/<num>')
def detail(num):
    for president in presidents_list:
        if president['Presidency'] == num:
            pres_dict = president
            break
    # a little bonus function, imported
    ord = make_ordinal( int(num) )
    return render_template('president.html', pres=pres_dict, ord=ord, the_title=pres_dict['President'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
