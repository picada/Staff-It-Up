from flask import render_template, request, redirect, url_for
from application import app

from flask_login import login_user, logout_user, current_user

@app.route("/")
def index():
        return render_template("index.html")
