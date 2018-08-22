from flask_wtf import FlaskForm
from wtforms import StringField, Form, validators
from wtforms_components import TimeField

class AssignmentForm(FlaskForm):
    role = StringField("Työtehtävä (keikkavastaava, rastiohjaaja tms.)", [validators.Length(min=2, message="Työtehtävän tulee olla vähintään 2 merkkiä pitkä"),
                                                        validators.Length(max=144, message="Työtehtävän pituus voi olla maksimissaan 144 merkkiä")])
    starttime = TimeField("Alkaa", [validators.Required(message="Syötä aika muodossa HH:MM")], format='%H:%M')
    endtime = TimeField("Päättyy", [validators.Required(message="Syötä aika muodossa HH:MM")], format='%H:%M')

    class Meta:
        csrf = False
