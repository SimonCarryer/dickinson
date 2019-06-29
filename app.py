from flask import Flask, jsonify, redirect, url_for, request, render_template
from flask_cors import CORS
import random

with open('deep_dickinson.txt', 'r') as f:
    poems = [p for p in f.read().split('<|endoftext|>') if len(p) > 10]

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def poem():
    poem = random.choice(poems)
    return render_template('poem.html', poem=poem)