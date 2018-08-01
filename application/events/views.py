from application import app, db
from flask import redirect, render_template, request, url_for
from application.events.models import Event
import datetime

@app.route("/events", methods=["GET"])
def events_index():
    return render_template("events/list.html", events = Event.query.all())

@app.route("/events/new/")
def events_form():
    return render_template("events/new.html")

@app.route("/events/<event_id>/", methods=["POST"])
def events_set_staffed(event_id):

    e = Event.query.get(event_id)
    e.staffed = True
    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/events/", methods=["POST"])
def events_create():
    print(request.form.get("type"))
    print(request.form.get("date"))
    print(request.form.get("pax"))
    print(request.form.get("info"))

    type = request.form.get("type")
    date = request.form.get("date")
    dateformat = datetime.datetime.strptime(date, "%Y-%m-%d")
    pax = request.form.get("pax")
    info = request.form.get("info")

    e = Event(type, dateformat, 2, info)
    print(e)

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("events_index"))
