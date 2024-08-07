#!/usr/bin/python3
"""DBStorage module"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """class that manages storage of models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a dbStorage instance"""
        USER = os.getenv('HBNB_MYSQL_USER')
        PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        ENV = os.getenv('HBNB_ENV')

        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            USER, PWD, HOST, DB
        )

        self.__engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{type(obj).__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for class_type in classes:
                objs = self.__session.query(class_type).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
