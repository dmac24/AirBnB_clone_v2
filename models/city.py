#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from tkinter import CASCADE
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    type_of_storage = getenv('HBNB_TYPE_STORAGE')
    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete, delete-orphan",
                              backref="cities")
    else:
        name = ''
        state_id = ''
