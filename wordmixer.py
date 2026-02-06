from flask import Flask, render_template, request

app = Flask(__name__)

def mix_word(word):
    return word

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mix')
def result():
    word = request.args.get('word', '')
    wordmixed = mix_word(word)
    return wordmixed