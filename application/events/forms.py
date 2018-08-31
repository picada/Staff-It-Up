from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, Form, validators
from wtforms.fields.html5 import DateField

class EventForm(FlaskForm):
    type = StringField("Tapahtuman tyyppi / nimi", [validators.Length(min=2, message="Nimen tulee olla vähintään 2 merkkiä pitkä"),
                                                        validators.Length(max=144, message="Nimen pituus voi olla maksimissaan 144 merkkiä")])
    date = DateField("Tapahtuman päivämäärä", [validators.Required(message="Syötä päivämäärä muodossa VVVV-kk-pp")], format='%Y-%m-%d')
    pax = IntegerField("Tapahtuman henkilömäärä", [validators.NumberRange(min=1, max=3000, message="Syötä numero väliltä 1 - 3000")])
    info = TextAreaField("Muu info (paikka, kesto, muut lisätiedot)", [validators.Length(max=500, message="Syöte liian pitkä, maksimipituus 500 merkkiä")])

    class Meta:
        csrf = False

class EventEditForm(FlaskForm):
    pax = IntegerField("Tapahtuman henkilömäärä", [validators.NumberRange(min=1, max=3000, message="Syötä numero väliltä 1 - 3000")])
    info = TextAreaField("Muu info (paikka, kesto, muut lisätiedot)", [validators.Length(max=500, message="Syöte liian pitkä, maksimipituus 500 merkkiä")])
    class Meta:
        csrf = False
