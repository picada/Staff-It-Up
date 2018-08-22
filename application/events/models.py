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

    def find_unstaffed_upcoming_events():
        stmt = text("SELECT event.type, event.date FROM event "
                    "WHERE event.staffed = '0' "
                    "GROUP BY event.type, event.date")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"type":row[0], "date":row[1]})

        return response
