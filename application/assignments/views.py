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

@app.route("/admin/assignments/<event_id>/<assignment_id>/delete", methods=["POST"])
@login_required(role="admin")
def assignment_delete(assignment_id, event_id):

    a = Assignment.query.get(assignment_id)
    registrations = a.registrations

    for reg in registrations:
        db.session.delete(reg)

    db.session.delete(a)
    db.session().commit()

    return redirect(url_for("event_details", event_id=event_id))

@app.route("/admin/registrations/<event_id>/")
@login_required(role="admin")
def registrations_list(event_id):

    e = Event.query.get(event_id)
    assignments = e.assignments

    return render_template("admin/assignments/list.html", assignments=assignments, event=e)

@app.route("/user/assignments/<event_id>/<assignment_id>", methods=["POST"])
@login_required(role="user")
def reg_create(assignment_id, event_id):

    a = AssignmentRegistration.query.filter_by(account_id=current_user.id, assignment_id=assignment_id).first()

    if not a:

        reg = AssignmentRegistration(current_user.id, assignment_id)

        db.session().add(reg)
        db.session().commit()

    return redirect(url_for("event_details_user", event_id=event_id))

@app.route("/user/assignments/<event_id>/<assignment_id>/delete", methods=["POST"])
@login_required(role="user")
def reg_delete(assignment_id, event_id):

    r = AssignmentRegistration.query.filter_by(account_id=current_user.id, assignment_id=assignment_id).first()

    db.session.delete(r);
    db.session().commit()

    return redirect(url_for("event_details_user", event_id=event_id))

@app.route("/user/assignments/delete/<assignment_id>", methods=["POST"])
@login_required(role="user")
def reg_delete_from_list(assignment_id):

    r = AssignmentRegistration.query.filter_by(account_id=current_user.id, assignment_id=assignment_id).first()

    db.session.delete(r);
    db.session().commit()

    return redirect(url_for("reg_userlist"))

@app.route("/admin/assignments/<event_id>/<assignment_id>/<account_id>", methods=["POST"])
@login_required(role="admin")
def reg_confirm_or_cancel(account_id, assignment_id, event_id):

    r = AssignmentRegistration.query.filter_by(account_id=account_id, assignment_id=assignment_id).first()
    if r.confirmed == False:
        r.confirmed = True
    else:
        r.confirmed = False
    db.session().commit()

    return redirect(url_for("registrations_list", event_id=event_id))

@app.route("/user/assignments", methods=["GET"])
@login_required(role="user")
def reg_userlist():
        return render_template("user/assignments/list.html", assignments=Assignment.find_unconfirmed_registrations_for_coming_events(user_id=current_user.id))
