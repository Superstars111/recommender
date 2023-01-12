import sqlalchemy as sqa
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin, LoginManager
from app import db

login = LoginManager()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = sqa.Column(sqa.Integer(), primary_key=True, index=True)
    email = sqa.Column(sqa.String(), unique=True, nullable=False)
    username = sqa.Column(sqa.String(), unique=True, nullable=False)
    password_hash = sqa.Column(sqa.String(), nullable=False)


class Media(db.Model):
    __tablename__ = "media"

    id = sqa.Column(sqa.Integer(), primary_key=True, index=True)
    title = sqa.Column(sqa.String(), nullable=False)
    type = sqa.Column(sqa.Integer(), nullable=False)  # Book, movie, anime, manga, video game, webcomic, song, visual novel, other
    # Possibly include subclasses for different media types
    # length
    # cost


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    id = sqa.Column(sqa.Integer(), primary_key=True, index=True)

    # Sender
    sent_by = sqa.Column(sqa.Integer(), sqa.ForeignKey("users.id"), nullable=False)
    sender_priority = sqa.Column(sqa.Integer())
    notes = sqa.Column(sqa.Text())  # Include sections and/or prompts for why you'd like it, what it's similar to, etc.

    # Receiver
    sent_to = sqa.Column(sqa.Integer(), sqa.ForeignKey("users.id"), nullable=False)
    personal_priority = sqa.Column(sqa.Integer())

    # Media
    version_specific = sqa.Column(sqa.Boolean())  # e.g., "I recommend SPECIFICALLY the anime, not the manga"
