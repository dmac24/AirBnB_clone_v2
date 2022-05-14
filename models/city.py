#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Atributtes to create a class table city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states_id'),
                      nullable=False)
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
