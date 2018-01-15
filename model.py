from flask_sqlalchemy import SQLAlchemy

from passlib.hash import bcrypt

db = SQLAlchemy()

# Model defintions


class User(db.Model):
    """ User info """

    __tablename__ = "users"

    # attributes for users
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    profile_img = db.Column(db.String(200))
    password = db.Column(db.String(200), nullable=False)
    update_time = db.Column(db.Integer)
    phone_num = db.Column(db.String(15))
    email = db.Column(db.String(100))
    subscribed = db.Column(db.Boolean, nullable=False)
    api_etag = db.Column(db.String(100))

    def __repr__(self):  # pragma: no cover
        return "<User username= %s>" % (self.username)


class Venue(db.Model):
    """ Music veune info """

    __tablename__ = "venues"


class Rating(db.Model):
    """ Users ratings of venues """

    __tablename__ = "ratings"

