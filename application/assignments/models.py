from application import db

from sqlalchemy.sql import text
import datetime

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.Time, nullable=False)
    endtime = db.Column(db.Time, nullable=False)
    role = db.Column(db.String(144), nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'),
       nullable=False)

    users = db.relationship("User", secondary="account_assignment")
    registrations = db.relationship("AssignmentRegistration", backref='assignment', lazy=True)

    def __init__(self, start, end, role, event):
        self.starttime = start
        self.endtime = end
        self.role = role
        self.event_id = event

    @staticmethod
    def check_reg_existence(user, assignment):

        r = AssignmentRegistration.query.filter_by(account_id=user, assignment_id=assignment).first()

        if r:
            return True
        else:
            return False

    @staticmethod
    def check_reg_confirmed(user, assignment):

        r = AssignmentRegistration.query.filter_by(account_id=user, assignment_id=assignment).first()

        if r and r.confirmed == True:
            return True
        else:
            return False

    @staticmethod
    def find_unconfirmed_registrations(assignment_id):

        stmt = text("SELECT account.id, account.name, assignment.id, account_assignment.regtime "
                    "FROM account, assignment, account_assignment "
                    "WHERE assignment.id = :id "
                    "AND assignment.id = account_assignment.assignment_id "
                    "AND account.id = account_assignment.account_id "
                    "AND account_assignment.confirmed = '0' "
                    "GROUP BY account.name "
                    "ORDER BY account_assignment.regtime")
        res = db.engine.execute(stmt, id=assignment_id)

        response = []
        for row in res:
            time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y klo %H:%M')
            response.append({"account_id":row[0], "name":row[1], "assignment_id":row[2], "regtime":time})

        return response

    @staticmethod
    def find_confirmed_registrations(assignment_id):

        stmt = text("SELECT account.id, account.name, account.email, account.phone, assignment.id "
                    "FROM account, assignment, account_assignment "
                    "WHERE assignment.id = :id "
                    "AND assignment.id = account_assignment.assignment_id "
                    "AND account.id = account_assignment.account_id "
                    "AND account_assignment.confirmed = '1' "
                    "GROUP BY account.name "
                    "ORDER BY account_assignment.regtime")
        res = db.engine.execute(stmt, id=assignment_id)

        response = []
        for row in res:
            response.append({"account_id":row[0], "name":row[1], "email":row[2], "phone":row[3], "assignment_id":row[4]})
        return response


class AssignmentRegistration(db.Model):

    __tablename__ = "account_assignment"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'), primary_key=True)
    regtime = db.Column(db.DateTime, default=db.func.current_timestamp())
    confirmed = db.Column(db.Boolean, nullable=False)

    def __init__(self, user, assignment):
        self.account_id = user
        self.assignment_id = assignment
        self.confirmed = False
