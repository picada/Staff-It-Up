from application import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(144), nullable=False)
    date = db.Column(db.Date, nullable=False)
    pax = db.Column(db.Integer)
    info = db.Column(db.String(500))
    staffed = db.Column(db.Boolean, nullable=False)

    def __init__(self, type, date, pax, info):
        self.type = type
        self.date = date
        self.pax = pax
        self.info = info
        self.staffed = False
