from application import db

from sqlalchemy.sql import text

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(144), nullable=False)
    date = db.Column(db.Date, nullable=False)
    pax = db.Column(db.Integer)
    info = db.Column(db.String(500))
    staffed = db.Column(db.Boolean, nullable=False)

    assignments = db.relationship("Assignment", backref='event', lazy=True)

    def __init__(self, type, date, pax, info):
        self.type = type
        self.date = date
        self.pax = pax
        self.info = info
        self.staffed = False

    def print_date():
        return self.date.strftime("%d.%m.%Y")

    @staticmethod
    def find_unstaffed_upcoming_events():

        response = Event.query.filter(Event.staffed=='0', Event.date > db.func.current_date()).order_by(Event.date).all()

        return response
