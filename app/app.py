from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello/<string:name>")
def hello(name=None):
    return render_template("app.html", name=name)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")