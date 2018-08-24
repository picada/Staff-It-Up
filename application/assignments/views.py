from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, current_user

from application.assignments.models import Assignment
from application.assignments.models import AssignmentRegistration
from application.assignments.forms import AssignmentForm
from application.events.models import Event
from application.events.forms import EventForm
from application.auth.models import User
import datetime

@app.route("/assignments/<int:event_id>", methods=["POST"])
@login_required(role="admin")
def assignment_create(event_id):
    form = AssignmentForm(request.form)

    if not form.validate():
            return render_template("admin/events/event.html", event=Event.query.get(event_id), form=form)

    a = Assignment(form.starttime.data, form.endtime.data, form.role.data, event_id)

    print(a)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("event_details", event_id=event_id))

# @app.route("/user/assignments/<int:event_id>", methods=["POST"])
# @login_required(role="user")
# def reg_create(assignment_id, event_id):
#
#     a = AssignmentRegistration.query.filter_by(account_id=current_user.id, assignment_id=assignment_id).first()
#
#     print(a)
#
#     if not a:
#         db.session().add(a)
#         db.session().commit()
#
#     reg = AssignmentRegistration(current_user.id, 3)
#
#     db.session().add(reg)
#     db.session().commit()
#
#     return redirect(url_for("event_details_user", event_id=event_id))
