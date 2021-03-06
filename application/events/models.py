from application import db

from sqlalchemy.sql import text
import datetime
from monthdelta import monthdelta

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

    @staticmethod
    def find_unstaffed_events_one_month():

        date = datetime.datetime.now() + monthdelta(1)

        response = Event.query.filter(Event.staffed=='0', Event.date > db.func.current_date(),
                        Event.date < date).order_by(Event.date).all()

        return response

    @staticmethod
    def find_confirmed_registrations(event_id):

        stmt = text("SELECT account.id, account.name, account.email, account.phone, assignment.id, assignment.role, assignment.starttime, assignment.endtime, event.id "
                    "FROM account, assignment, account_assignment, event "
                    "WHERE event.id = :id "
                    "AND assignment.event_id = event.id "
                    "AND assignment.id = account_assignment.assignment_id "
                    "AND account.id = account_assignment.account_id "
                    "AND account_assignment.confirmed = '1' "
                    "ORDER BY assignment.role")
        res = db.engine.connect().execute(stmt, id=event_id)

        response = []
        for row in res:
            response.append({"account_id":row[0], "name":row[1], "email":row[2],
                    "phone":row[3], "assignment_id":row[4], "assignment_role":row[5],
                    "assignment_start":str(row[6]), "assignment_end":str(row[7]), "event_id":row[8]})
        return response


    @staticmethod
    def find_events_with_unconfirmed_registrations():

        stmt = text("SELECT event.id, event.type, event.date, COUNT(*) "
                    "FROM event "
                    "INNER JOIN assignment ON event.id = assignment.event_id "
                    "INNER JOIN account_assignment ON account_assignment.assignment_id = assignment.id "
                    "WHERE event.staffed = '0' "
                    "AND event.date > CURRENT_DATE "
                    "AND account_assignment.confirmed = '0' "
                    "GROUP BY event.id "
                    "HAVING COUNT(*) > 0 "
                    "ORDER BY event.date")
        res = db.engine.connect().execute(stmt)


        response = []
        for row in res:
            response.append({"event_id":row[0], "event_type":row[1],
                    "event_date":datetime.datetime.strptime(str(row[2]), "%Y-%m-%d"),
                    "registrations":row[3]})
        return response

    @staticmethod
    def has_assignments(event_list):

        for event in event_list:
            if event.assignments:
                return True

        return False
