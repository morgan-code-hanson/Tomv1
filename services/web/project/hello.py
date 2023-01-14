# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
@app.route("/json")
def hello_world():
    return jsonify(hello="world")

