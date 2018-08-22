from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.assignments.models import Assignment
from application.events.models import Event
from application.events.forms import EventForm
from application.assignments.forms import AssignmentForm
import datetime

@app.route("/assignments/<int:event_id>", methods=["POST"])
@login_required
def assignment_create(event_id):
    form = AssignmentForm(request.form)

    if not form.validate():
            return render_template("events/event.html", event=Event.query.get(event_id), form=form)

    a = Assignment(form.starttime.data, form.endtime.data, form.role.data, event_id)

    print(a)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("event_details", event_id=event_id))
