from application import db

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
