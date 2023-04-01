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

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    director = Column(String(70), nullable=False)
    year = Column(String(4))
    rating= Column(Float)

class Affiliation(Base):
    __tablename__='affiliation'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(700))
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    population =Column (Integer)
    description = Column(String(300))
    climate = Column(String(200))
    terrain = Column(String(50))
    history = Column(String(700))
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)
    affiliation_id = Column(Integer, ForeignKey('affiliation.id'))
    affiliation = relationship(Affiliation)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    description = Column(String(500))
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)
    affiliation_id = Column(Integer, ForeignKey('affiliation.id'))
    affiliation = relationship(Affiliation)

class Gender(Base):
    __tablename__ = 'gender'
    id= Column(Integer, primary_key=True)
    gender = Column(String(50))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    description = Column(String(500))
    dimensions = Column(Float)
    specie_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    gender = relationship(Gender)
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)
    affiliation_id = Column(Integer, ForeignKey('affiliation.id'))
    affiliation = relationship(Affiliation)

class Creatures(Base):
    __tablename__ ='creatures'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    dimensions = Column(Float)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    gender = relationship(Gender)

class Nature(Base):
    __tablename__ = 'nature'
    id = Column(Integer, primary_key=True)
    specie_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters= relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
