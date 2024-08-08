#!/usr/bin/python3
"""State Module"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            city_in_state = []
            for v in storage.all(City).values():
                if v.state_id == self.id:
                    city_in_state.append(v)
            return city_in_state
