from flask import render_template
from application import app
from application.events.models import Event

@app.route("/")
def index():
    return render_template("index.html", needs_staff=Event.find_unstaffed_upcoming_events())
