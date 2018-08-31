from flask import render_template, request, redirect, url_for
from application import app

from flask_login import login_user, logout_user, current_user

from application.events.models import Event
from application.assignments.models import Assignment
from application.auth.forms import LoginForm

@app.route("/")
def index():
    if current_user.is_authenticated:
        upcoming_shifts=Assignment.find_confirmed_registrations_for_coming_events(user_id=current_user.id)[:5]
    else:
        upcoming_shifts=[]

    return render_template("index.html",
            needs_staff=Event.find_unstaffed_events_one_month(),
            form = LoginForm(),
            has_registrations=Event.find_events_with_unconfirmed_registrations(),
            next_five_shifts=upcoming_shifts)
