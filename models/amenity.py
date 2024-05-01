#!/usr/bin/python3i
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class Amenity"""
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", back_populates="amenities",
                                       secondary="place_amenity")
    else:
        name = ""
