#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """return cities in a state"""
            dict1 = self.all(City)
            cities_list = []
            for key, value in dict1.items():
                if value['state_id'] == self.id:
                    cities_list.append[value]
            return cities_list
