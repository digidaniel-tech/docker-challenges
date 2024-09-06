import models.base as base

from flask_restful import fields
from sqlalchemy import Column, Integer, String

user_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'email': fields.String
}

class User(base.Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  email = Column(String)
