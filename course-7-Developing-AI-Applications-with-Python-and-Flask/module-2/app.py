from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b> First Flask App </b>"

def index():
    return jsonify(message="Hello, World!")