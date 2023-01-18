#!/usr/bin/python3

""" starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Prints C followed by the value of the text variable """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ Prints Python, followed by the value of the text variable """
    return "Python {:s}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Prints n is a number, only if n is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
