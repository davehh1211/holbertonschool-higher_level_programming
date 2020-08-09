#!/usr/bin/python3
"""[summary]
    """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """[summary]

    Args:
    Base ([type]): [description]
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128))
    cities = relationship('City')
