#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """atributtes to create a State Table
    in the database"""
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade="all, \
                              delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Method that return all the
            cities in the currently State"""
            from models import storage
            cities_of_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_of_state.append(value)
            return cities_of_state
