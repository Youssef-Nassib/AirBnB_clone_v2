#!/usr/bin/python3
"""city module"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """city class objects"""

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

