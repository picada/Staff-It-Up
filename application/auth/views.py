from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import NewUserForm
from application.auth.forms import UpdateUserForm
from application.auth.forms import UpdatePasswordForm
from application.auth.models import Role
from application.auth.models import UserRole
from application.events.models import Event


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return redirect(url_for("index"))

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("index.html", form = LoginForm(),
                               error = "Käyttäjätunnus ja/tai salasana virheellinen")

    print("Käyttäjä " + user.name + " tunnistettiin")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/new/")
def newUser_form():
    return render_template("auth/new.html", form = NewUserForm())

@app.route("/admin/auth/new/")
def newUser_admin():
    return render_template("admin/auth/new.html", form = NewUserForm())


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

@app.route("/admin/auth/new/", methods=["POST"])
@login_required(role="admin")
def user_create_as_admin():
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

    if form.admin.data == True:
         role = Role.query.filter_by(name="admin").first()

    user_role = UserRole(user.id, role.id)
    db.session.add(user_role)
    db.session.commit()

    return redirect(url_for("list_users"))

@app.route("/admin/auth/users")
@login_required(role="admin")
def list_users():
    users = User.query.order_by(User.name).all()
    return render_template("admin/auth/list.html", users=users)

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/admin/auth/delete/<user_id>/", methods=["POST"])
@login_required(role="admin")
def user_delete(user_id):

    User.delete_user(user_id)

    return redirect(url_for("list_users"))


@app.route("/auth/update/<user_id>/", methods=["GET", "POST"])
@login_required("ANY")
def user_update(user_id):
    user = User.query.get(user_id)

    if request.method == "GET":
        form = UpdateUserForm(obj=user)
        password_form = UpdatePasswordForm()

        return render_template("auth/update.html", form=form, password_form=password_form, user=user)

    form = UpdateUserForm(request.form)

    if not form.validate():
        return render_template("auth/update.html", form=form, password_form=UpdatePasswordForm(), user=user)

    user.name = form.name.data
    user.phone = form.phone.data
    user.email = form.email.data

    if user.role_ok("admin") and form.admin.data == True:
        User.switch_roles("admin", "user", user_id)
        flash('Tietojen päivittäminen onnistui')
        return redirect(url_for("user_update", user_id=user_id))
    elif user.role_ok("user") and form.admin.data == True:
        User.switch_roles("user", "admin", user_id)
        flash('Tietojen päivittäminen onnistui')
        return redirect(url_for("user_update", user_id=user_id))
    else:
        db.session().commit()
        flash('Tietojen päivittäminen onnistui')
        return redirect(url_for("user_update", user_id=user_id))

@app.route("/auth/update_password/<user_id>/", methods=["POST"])
@login_required("ANY")
def password_update(user_id):
    user = User.query.get(user_id)
    form = UpdateUserForm(obj=user)
    password_form = UpdatePasswordForm(request.form)

    if not password_form.validate():
        return render_template("auth/update.html", form=form, password_form=password_form, user=user)

    user = User.query.filter_by(id=user_id, password=password_form.currentpassword.data).first()
    if not user:
        flash('Syöttämäsi nykyinen salasana on virheellinen')
        return redirect(url_for("user_update", user_id=user_id))

    user.password=password_form.newpassword.data
    db.session().commit()
    flash('Salasanan päivittäminen onnistui')
    return redirect(url_for("user_update", user_id=user_id))
