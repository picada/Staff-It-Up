from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, Form, validators
from wtforms.fields.html5 import DateField

class EventForm(FlaskForm):
    type = StringField("Tapahtuman tyyppi / nimi", [validators.Length(min=2, message="Nimen tulee olla vähintään 2 merkkiä pitkä")])
    date = DateField("Tapahtuman päivämäärä")
    pax = IntegerField("Tapahtuman henkilömäärä", [validators.NumberRange(min=1, max=3000, message="Syötä numero väliltä 1 - 3000")])
    info = TextAreaField("Muu info (paikka, kesto, muut lisätiedot)")

    class Meta:
        csrf = False
