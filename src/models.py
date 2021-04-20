import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
=======
    user_name = Column(String(50))
    email = Column(String(250), unique=True)
    password = Column(String(10), nullable=False)
    loggin = Column(String(20))
>>>>>>> 9620197a16395b592df3a8338b031cbef342fa06

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
=======
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('person.id'))
    favorites = relationship(User)
>>>>>>> 9620197a16395b592df3a8338b031cbef342fa06

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    birth_year = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    name = Column(String(250), nullable=False)
    user = relationship("user")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')