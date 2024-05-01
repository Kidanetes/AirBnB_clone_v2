#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""
        @property
        def cities(self):
            """list of cities in a state"""
            from models import storage
            cities_list = []
            objs = storage.all(City).values()
            for i in objs:
                if self.id == i.state_id:
                    cities_list.append(i)
            return cities_list
