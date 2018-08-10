from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Etu- ja sukunimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    email = EmailField("Sähköpostiosoite")
    phone = StringField("Puhelinnumero")

    class Meta:
        csrf = False
