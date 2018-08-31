from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, BooleanField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Etu- ja sukunimi", [validators.Length(min=4, message="Nimen tulee olla vähintään 4 merkkiä pitkä"),
                                                validators.Length(max=144, message="Syöte liian pitkä, sallittu merkkimäärä 144")])
    username = StringField("Käyttäjätunnus", [validators.Length(min=4, max=10, message="Käyttäjätunnuksen tulee olla 4-20 merkkiä pitkä")])
    password = PasswordField("Salasana", [validators.Length(min=6, message="Salasanan tulee olla vähintään 6 merkkiä pitkä"),
                                                validators.Length(max=144, message="Salasana liian pitkä, sallittu merkkimäärä 144"),
                                                validators.equal_to('confirm', message='Salasanojen tulee täsmätä')])
    confirm  = PasswordField('Vahvista salasana')
    email = EmailField("Sähköpostiosoite", [validators.Email(message="Syötä sähköpostiosoite oikeassa muodossa (tunnus@domain.fi)"),
                                                validators.Length(max=144, message="Sähköpostiosoite on liian pitkä, sallittu merkkimäärä 144")])
    phone = StringField("Puhelinnumero", [validators.Length(min=6, max=20, message="Puhelinnumeron tulee olla 6-20 merkkiä pitkä")])
    admin = BooleanField("Luodaanko ylläpitäjätunnus? (oletus:työntekijä)")

    class Meta:
        csrf = False

class UpdateUserForm(FlaskForm):
    name = StringField("Etu- ja sukunimi", [validators.Length(min=4, message="Nimen tulee olla vähintään 4 merkkiä pitkä"),
                                                validators.Length(max=144, message="Syöte liian pitkä, sallittu merkkimäärä 144")])
    email = EmailField("Sähköpostiosoite", [validators.Email(message="Syötä sähköpostiosoite oikeassa muodossa (tunnus@domain.fi)"),
                                                validators.Length(max=144, message="Sähköpostiosoite on liian pitkä, sallittu merkkimäärä 144")])
    phone = StringField("Puhelinnumero", [validators.Length(min=6, max=20, message="Puhelinnumeron tulee olla 6-20 merkkiä pitkä")])
    admin = BooleanField()

    class Meta:
        csrf = False

class UpdatePasswordForm(FlaskForm):
    currentpassword = PasswordField("Nykyinen salasana", [validators.InputRequired(message="Syötä nykyinen salasana")])
    newpassword = PasswordField("Uusi salasana", [validators.Length(min=6, message="Salasanan tulee olla vähintään 6 merkkiä pitkä"),
                                                validators.Length(max=144, message="Salasana liian pitkä, sallittu merkkimäärä 144"),
                                                validators.equal_to('confirm', message='Salasanojen tulee täsmätä')])
    confirm  = PasswordField('Vahvista uusi salasana')

    class Meta:
        csrf = False
