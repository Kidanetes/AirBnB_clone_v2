#!/usr/bin/python3
"""this module contains the defintion of
db storage"""


from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DBStorage class contains a database storage for
    AirBnB console
    Attributes:
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        db1 = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        self.__engine = (create_engine('mysql+mysqldb://{}:{}@{}/{}'
                         .format(user, passwd, host, db1),
                         pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all objects of the same class
        if th class is specified or all objects of
        every class if cls is none"""
        dict1 = {}
        if cls is not None:
            objs = self.__session.query(cls)
            for i in objs:
                key = f"{i.__class__.__name__}.{i.id}"
                #if '_sa_instance_state' in i.__dict__:
                #    del i.__dict__['_sa_instance_state']
                dict1[key] = i
        else:
            for j in [State, City, User, Place, Review, Amenity]:
                objs = self.__session.query(j)
                for i in objs:
                    key = f"{i.__class__.__name__}.{i.id}"
                    #if '_sa_instance_state' in i.__dict__:
                    #    del i.__dict__['_sa_instance_state']
                    dict1[key] = i
        return dict1

    def new(self, obj):
        """create new obj and and add it to the session"""
        self.__session.add(obj)

    def save(self):
        """commits every change on the session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all defined tables and creates a session"""
        Base.metadata.create_all(self.__engine)
        a = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(a)
        self.__session = Session()
