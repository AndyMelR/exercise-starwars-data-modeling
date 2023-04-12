import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(16), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(60), nullable= False)
    password = Column(String(10), nullable=False)

class Basic_data(Base):
    __tablename__ = 'basic_data'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(700))

class Films(Base):
    __tablename__ = 'films'
    director = Column(String(70), nullable=False)
    year = Column(String(4))
    rating= Column(Float)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    film_basic_data = relationship(Basic_data)

class Affiliation(Base):
    __tablename__ = 'affiliation'
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    affiliation_basic_data = relationship(Basic_data)
   
class Planet(Base):
    __tablename__ = 'planet'
    population =Column (Integer)
    climate = Column(String(200))
    terrain = Column(String(50))
    history = Column(String(700))
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    planet_basic_data = relationship(Basic_data)

class Species(Base):
    __tablename__ = 'species'
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    specie_basic_data = relationship(Basic_data)

class Gender(Base):
    __tablename__ = 'gender'
    id= Column(Integer, primary_key=True)
    name = Column(String(50))

class Characters(Base):
    __tablename__ = 'characters'
    dimensions = Column(Float)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    character_basic_data = relationship(Basic_data)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    character_gender = relationship(Gender)
    
class Creatures(Base):
    __tablename__ ='creatures'
    dimensions = Column(Float)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    creature_basic_data = relationship(Basic_data)

class Vehicles(Base):
    __tablename__='vehicles'
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    vehicle_basic_data = relationship(Basic_data)
    dimensions = Column(Float)

class Droids(Base):
    __tablename__='droids'
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    droid_basic_data = relationship(Basic_data)

class Weapons(Base):
    __tablename__='weapons'
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)
    weapons_basic_data = relationship(Basic_data)

class favorite_characters(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'), primary_key=True)


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
