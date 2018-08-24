from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.events.models import Event
from application.events.forms import EventForm
from application.assignments.forms import AssignmentForm
from application.assignments.models import Assignment
import datetime

@app.route("/admin/events", methods=["GET"])
@login_required(role="admin")
def events_index():
    events = Event.query.all()
    return render_template("admin/events/list.html", events = Event.query.order_by(Event.date).all())

@app.route("/user/events", methods=["GET"])
@login_required(role="user")
def events_userindex():
    events = Event.query.all()
    return render_template("user/events/list.html", events = Event.query.order_by(Event.date).all())

@app.route("/admin/events/new/")
@login_required(role="admin")
def events_form():
    return render_template("admin/events/new.html", form = EventForm())

@app.route("/admin/events/<event_id>/", methods=["POST"])
@login_required(role="admin")
def events_set_staffed(event_id):

    e = Event.query.get(event_id)
    if e.staffed == False:
        e.staffed = True
    else:
        e.staffed = False

    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/admin/events/<event_id>/details", methods=["GET"])
@login_required(role="admin")
def event_details(event_id):
    event = Event.query.get(event_id)
    return render_template("admin/events/event.html", event=event, form=AssignmentForm(), assignments=event.assignments)

@app.route("/user/events/<event_id>/details", methods=["GET"])
@login_required(role="user")
def event_details_user(event_id):
    event = Event.query.get(event_id)
    return render_template("user/events/event.html", event=event, assignments=event.assignments)


@app.route("/admin/events/delete/<event_id>/", methods=["POST"])
@login_required(role="admin")
def events_delete(event_id):

    e = Event.query.get(event_id)
    assignments = e.assignments
    for assignment in assignments:
        db.session.delete(assignment)
        db.session().commit()

    db.session.delete(e);
    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/admin/events/", methods=["POST"])
@login_required(role="admin")
def events_create():
    form = EventForm(request.form)

    if not form.validate():
        return render_template("admin/events/new.html", form = form)

    e = Event(form.type.data, datetime.datetime.strptime(str(form.date.data), "%Y-%m-%d"), form.pax.data, form.info.data)
    print(e)

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("events_index"))
