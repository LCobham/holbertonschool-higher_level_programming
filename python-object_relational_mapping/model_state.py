#!/usr/bin/python3
"""
    This is a module that defines a state class
    with SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class to connect with SQL database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
