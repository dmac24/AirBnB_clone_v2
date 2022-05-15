#!/usr/bin/python3
"""
Module that define Class DBStorage which
can help us to manipulate data in a database
"""
import os
from os import getenv
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import models
from models.base_model import Base


class DBStorage:
    """
    Class that defines class to map and
    store in a database.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialice enviroment variables and create
        engine with database"""

        user = getenv('HBHB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(host, user, password, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.drop_all(self.__engine)

    def all(self, cls=None):
        """Method that return a dict with all elements from
        a specific class (cls), if it isn't find it return
        a dict with all elements of all classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        dictionary = {}

        if cls is None:
            search_result = self.__session.query(User, Place, State, City,
                                                 Amenity, Review).all()
        else:
            search_result = self.__session.query(cls).all()

        for object in search_result:
            dictionary[object.__class__.__name__ + '.' + object.id] = object

        return dictionary

    def new(self, obj):
        """method that add currently object
        to the database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """Method that add changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method that delete obj from the
        database current session"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """Reload the currently database
        session.
        """
        from sqlalchemy.orm import scoped_session
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(Session_factory)()

    def close(self):
        """Closes the storage engine"""
        self.__session.close()
