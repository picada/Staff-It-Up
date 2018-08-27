from flask import render_template, request, redirect, url_for
from application import app

from flask_login import login_user, logout_user, current_user

from application.events.models import Event
from application.auth.forms import LoginForm

@app.route("/")
def index():
        return render_template("index.html", needs_staff=Event.find_unstaffed_upcoming_events(), form = LoginForm())
