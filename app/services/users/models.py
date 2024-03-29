from flask_sqlalchemy import SQLAlchemy
""" Creating an Sqlqlchamy instance"""
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self, exclude=[]):
        _dict = {}
        for cols in self.__table__.columns:
            if cols.name not in exclude:
                _dict[cols.name] = self.__getattribute__(cols.name)
        return _dict
