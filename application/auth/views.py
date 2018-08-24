from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import NewUserForm
from application.auth.models import Role
from application.auth.models import UserRole
from application.events.models import Event


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "Käyttäjätunnus ja/tai salasana virheellinen")

    if not user.role_ok('user'):
        return render_template("auth/login.html", form = form,
                               error = "Tunnuksella ei ole työntekijäoikeuksia")

    print("Käyttäjä " + user.name + " tunnistettiin")

    login_user(user)
    return redirect(url_for("user_index"))

@app.route("/auth/login/admin", methods = ["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template("auth/adminlogin.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/adminlogin.html", form = form,
                               error = "Käyttäjätunnus ja/tai salasana virheellinen")

    if not user.role_ok('admin'):
        return render_template("auth/adminlogin.html", form = form,
                               error = "Tunnuksella ei ole ylläpito-oikeuksia")

    print("Käyttäjä " + user.name + " tunnistettiin")

    login_user(user)
    return redirect(url_for("admin_index"))

@app.route("/admin/index/")
@login_required(role="admin")
def admin_index():
    return render_template("admin/index.html", needs_staff=Event.find_unstaffed_upcoming_events())

@app.route("/user/index/")
@login_required(role="user")
def user_index():
    return render_template("user/index.html", needs_staff=Event.find_unstaffed_upcoming_events())

@app.route("/auth/new/")
def newUser_form():
    return render_template("auth/new.html", form = NewUserForm())

@app.route("/auth/new/", methods=["POST"])
def user_create():
    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()
    if user is not None:
        return render_template("auth/new.html", form = form,
                               error = "Käyttäjänimi on jo varattu")

    u = User(form.name.data, form.username.data, form.password.data, form.email.data, form.phone.data)

    db.session().add(u)
    db.session().commit()

    role = Role.query.filter_by(name="user").first()
    user = User.query.filter_by(username=u.username).first()

    if role is None:
        db.session.add(Role("user"))
        db.session.commit()
        role = Role.query.filter_by(name="user").first()

    user_role = UserRole(user.id, role.id)
    db.session.add(user_role)
    db.session.commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
