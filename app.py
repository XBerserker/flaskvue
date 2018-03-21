# coding=utf-8
from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)