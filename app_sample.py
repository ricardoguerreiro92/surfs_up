from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello World</br><a href= 'http://127.0.0.1:5000/universe'>Go to Hello Universe</a href>"

@app.route("/universe")
def hello_universe():
    return "Hello Universe"
