from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.events.models import Event
from application.events.forms import EventForm
import datetime

@app.route("/events", methods=["GET"])
@login_required
def events_index():
    return render_template("events/list.html", events = Event.query.all())

@app.route("/events/new/")
@login_required
def events_form():
    return render_template("events/new.html", form = EventForm())

@app.route("/events/<event_id>/", methods=["POST"])
@login_required
def events_set_staffed(event_id):

    e = Event.query.get(event_id)
    e.staffed = True
    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/events/<event_id>/details", methods=["GET"])
@login_required
def event_details(event_id):
    return render_template("events/event.html", event=Event.query.get(event_id))

@app.route("/events/delete/<event_id>/", methods=["POST"])
@login_required
def events_delete(event_id):

    e = Event.query.get(event_id)
    db.session.delete(e);
    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/events/", methods=["POST"])
@login_required
def events_create():
    form = EventForm(request.form)

    if not form.validate():
        return render_template("events/new.html", form = form)

    e = Event(form.type.data, datetime.datetime.strptime(str(form.date.data), "%Y-%m-%d"), form.pax.data, form.info.data)
    print(e)

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("events_index"))
