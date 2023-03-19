"""basic Flask app - demo of using a variable in a route"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/Albert">Click me!</a></p>'
    return greet + link

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'
    return personal + instruc

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)

# if you need to avoid using port 5000 - some Mac users -
# delete the first app.run() line above and
# un-comment the second app.run() line. Then use localhost:4999
