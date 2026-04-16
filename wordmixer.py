from flask import Flask, render_template
from wordmixer_service import MixWordService
import flask
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/mix', methods=['GET'])
def result():
    word = flask.request.args.get('word', '')
    sleep_time = int(os.getenv('SLEEP_TIME', '0'))
    time.sleep(sleep_time)
    wordmixed = MixWordService.mix_word(word)
    return wordmixed