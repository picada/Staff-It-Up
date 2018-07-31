from flask import render_template
from application import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def testpage():
    return render_template("test.html")
