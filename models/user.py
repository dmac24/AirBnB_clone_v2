#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    type_of_storage = getenv('HBNB_TYPE_STORAGE')
    if type_of_storage == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
