from flask import render_template
from application import app

from flask_login import login_user, logout_user

@app.route("/")
def index():
    return render_template("index.html")
