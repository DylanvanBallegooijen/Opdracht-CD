# Import what we need from flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/cow')
def cow():
    return 'MOoooOo! Im a COooooOW'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
