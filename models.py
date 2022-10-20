import sqlalchemy as sqa
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin, LoginManager
from .app import db


class User(UserMixin, db.Model):
    pass
