# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested


@app.route("/")
def index():
    return "Almost finished!!"


@app.route("/cow")
def cow():
    return "MOoooOo!"


@app.route("/dog")
def dog():
    return "Beware of this cuddling little doggy, Chester!!"
