#!/usr/bin/python3
"""review module"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """review class"""
    __tablename__ = 'reviews'

    place_id = Column(
        String(60), ForeignKey('places.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
