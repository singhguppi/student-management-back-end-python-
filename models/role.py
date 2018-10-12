# import sqlite3
from db import db


class RoleModel(db.Model):

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'id': self.id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_roles(cls):
        return cls.query.all()

    @classmethod
    def read_roles_by_role_name(cls, role_name):
        return cls.query.filter_by(name=role_name).all()