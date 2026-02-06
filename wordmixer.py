from flask import Flask, render_template, request
import random

app = Flask(__name__)

def mix_word(word):
    return ''.join(random.sample(word, k=len(word)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mix')
def result():
    word = request.args.get('word', '')
    wordmixed = mix_word(word)
    return wordmixed