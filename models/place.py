#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.review import Review
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    type_storage = getenv('HBNB_TYPE_STORAGE')
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))

    if type_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade="all, delete, delete-orphan",
                               backref='place')
        amenities = relationship(
            'Amenity', secondary='place_amenity', viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Get list of Reviews with the
            same id that the currently place
            """
            from models import storage
            list_reviews = []
            for review in storage.all(Review).values():
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            from models import storage
            return self.amenity_ids

        @amenities.setter
        def amenities(self, cls):
            from models.amenity import Amenity
            if cls.__class__ == Amenity:
                self.amenity_ids.append(cls.id)
