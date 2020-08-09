#!/usr/bin/python3
"""[summary]
    """
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """[summary]

    Args:
    Base ([type]): [description]
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)

    name = Column(String(128))
    cities = relationship('City')
