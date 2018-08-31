from application import db

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(144))
    phone = db.Column(db.String(20))

    roles = db.relationship("Role", secondary="account_role")
    registrations = db.relationship("AssignmentRegistration", backref='account', lazy=True)

    def __init__(self, name, username, password, email, phone):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def role_ok(self, role):
        for user_role in self.roles:
                    if user_role.name == role:
                        return True

    @staticmethod
    def delete_user(user_id):

        db.engine.connect().execute("DELETE FROM account_assignment WHERE account_assignment.account_id = :id", id=user_id)
        db.engine.connect().execute("DELETE FROM account_role WHERE account_role.account_id = :id", id=user_id)
        db.engine.connect().execute("DELETE FROM account WHERE account.id = :id", id=user_id)


    @staticmethod
    def switch_roles(role_one, role_two, user_id):

        r = Role.query.filter_by(name=role_one).first()
        user_role = UserRole.query.filter_by(account_id=user_id, role_id=r.id).first()
        db.session.delete(user_role)
        r = Role.query.filter_by(name=role_two).first()
        db.session.add(UserRole(user_id, r.id))
        db.session().commit()

class Role(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

class UserRole(db.Model):

    __tablename__ = "account_role"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)

    def __init__(self, user, role):
        self.account_id = user
        self.role_id = role
