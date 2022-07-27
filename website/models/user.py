from db import db
from flask_login import UserMixin


class User(db.Model,UserMixin):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    phone = db.Column(db.String(10))
    email = db.Column(db.String(50))
    password = db.Column(db.String(30))

    #links to the association table
    carpools = db.relationship('UserCarpool',back_populates='users')