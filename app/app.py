from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)

url_for('static', filename='app.css')

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('app.html', name=name)
