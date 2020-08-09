#!/usr/bin/python3
"""[summary]
    """
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """[summary]

    Args:
    Base ([type]): [description]
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
