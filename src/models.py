import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50))
    email = Column(String(250), unique=True)
    password = Column(String(10), nullable=False)
    loggin = Column(String(20))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('person.id'))
    favorites = relationship(User)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(10))
    eye_color = Column(String(10))
    height = Column(Integer)
    birth_year = Column(String(50))
    skin_color = Column(String(10))
    user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(50))
    diameter = Column(Integer)
    climate = Column(String(50))
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')