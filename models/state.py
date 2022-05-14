#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """atributtes to create a State Table
    in the database"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)    
    """ State class """
    name = ""
