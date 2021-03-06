from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///staffitup.db"
    app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Ole hyvä ja kirjaudu sisään käyttääksesi tätä toimintoa"

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False


            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles:
                    if user_role.name == role:
                        unauthorized = False
                        break

            if unauthorized:
                if role == "admin":
                    login_manager.login_message = "Ole hyvä ja kirjaudu sisään ylläpitäjätunnuksella käyttääksesi tätä toimintoa"
                if role == "user":
                    login_manager.login_message = "Ole hyvä ja kirjaudu sisään työntekijätunnuksella käyttääksesi tätä toimintoa"
                return login_manager.unauthorized()

            login_manager.login_view = "auth_login"

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from application import views

from application.events import models
from application.events import views

from application.auth  import models
from application.auth import views

from application.assignments import models
from application.assignments import views

try:
    db.create_all()

    from application.auth.models import Role

    role = Role.query.filter_by(name="admin").first()

    if not role:
        db.session.add(Role("admin"))
        db.session().commit()

    role = Role.query.filter_by(name="user").first()

    if not role:
        role = Role("admin")
        db.session.add(Role("user"))
        db.session().commit()

except:
    pass
