from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("salasana")

    class Meta:
        csrf = False
