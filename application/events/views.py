from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

from application.events.models import Event
from application.events.forms import EventForm
from application.assignments.forms import AssignmentForm
from application.assignments.models import Assignment
from application.assignments.models import AssignmentRegistration
import datetime

@app.route("/admin/events/<view>", methods=["GET"])
@login_required(role="admin")
def events_index(view):
    has_assignments = True
    if view=="needs_staff":
        events=Event.find_unstaffed_upcoming_events()
        if not Event.has_assignments(events):
            has_assignments = False
    if view=="upcoming":
        events=Event.query.filter(Event.date > db.func.current_date()).order_by(Event.date).all()
    if view=="past":
        events=Event.query.filter(Event.date < db.func.current_date()).order_by(Event.date.desc()).all()
    return render_template("admin/events/list.html", events = events, view=view, has_assignments=has_assignments)

@app.route("/user/events", methods=["GET"])
@login_required(role="user")
def events_userindex():
    needs_staff=Event.find_unstaffed_upcoming_events()
    has_assignments = Event.has_assignments(needs_staff)
    return render_template("user/events/list.html", needs_staff=needs_staff, has_assignments=has_assignments)

@app.route("/admin/events/new/")
@login_required(role="admin")
def events_form():
    return render_template("admin/events/new.html", form = EventForm())

@app.route("/admin/events/<event_id>/<view>", methods=["POST"])
@login_required(role="admin")
def events_set_staffed(event_id, view):

    e = Event.query.get(event_id)
    if e.staffed == False:
        e.staffed = True
    else:
        e.staffed = False

    db.session().commit()

    if view == "event":
        return redirect(url_for("event_details", event_id=event_id))

    return redirect(url_for("events_index", view=view))

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


@app.route("/admin/events/delete/<event_id>/<view>", methods=["POST"])
@login_required(role="admin")
def events_delete(event_id, view):

    e = Event.query.get(event_id)
    assignments = e.assignments
    for assignment in assignments:
        registrations = assignment.registrations
        for reg in registrations:
            db.session.delete(reg)
        db.session.delete(assignment)

    db.session.delete(e);
    db.session().commit()

    return redirect(url_for("events_index", view=view))

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

    return redirect(url_for("events_index", view="upcoming"))

@app.route("/admin/update/event/<event_id>/", methods=["GET", "POST"])
@login_required("admin")
def events_update(event_id):

    event = Event.query.get(event_id)

    if request.method == "GET":
        form = EventForm(obj=event)
        return render_template("admin/events/update.html", form=form, event=event)

    event = Event.query.get(event_id)

    form = EventForm(request.form)

    if not form.validate():
        return render_template("admin/events/update.html", form=form, event=event)

    event.type = form.type.data
    event.date = datetime.datetime.strptime(str(form.date.data), "%Y-%m-%d")
    event.pax = form.pax.data
    event.info = form.info.data

    db.session().commit()
    flash('Tapahtuman tietojen päivittäminen onnistui')
    return redirect(url_for("event_details", event_id=event_id))
