from application import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.Time, nullable=False)
    endtime = db.Column(db.Time, nullable=False)
    role = db.Column(db.String(144), nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'),
       nullable=False)

    users = db.relationship("User", secondary="account_assignment")

    def __init__(self, start, end, role, event):
        self.starttime = start
        self.endtime = end
        self.role = role
        self.event_id = event

    def check_reg_existence(self, user, assignment):

        r = AssignmentRegistration.query.filter_by(account_id=user, assignment_id=assignment).first()

        if r:
            return True
        else:
            return False


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
