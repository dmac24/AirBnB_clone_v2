#!/usr/bin/python3
"""Module that dfine State class
"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    type_of_storage = getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'states'

    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        name = ''

        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
