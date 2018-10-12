from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer)
    username = db.Column(db.String(80))
    full_name = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password, name, role_id):
        self.username = username
        self.password = password
        self.role_id = role_id
        self.full_name = name


    def json(self):
        return {'name': self.full_name, 'role_id':self.role_id, 'id': self.id}

    def add_user(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_users(cls):
        return cls.query.all()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(id=userid).first()
