#!/usr/bin/python3
""" Review module for the HBNB project """

from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    type_storage = getenv('HBNB_TYPE_STORAGE')
    if type_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
