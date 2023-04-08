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

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    population =Column (Integer)
    description = Column(String(300))
    climate = Column(String(200))
    terrain = Column(String(50))
    history = Column(String(700))

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    description = Column(String(500))

class Gender(Base):
    __tablename__ = 'gender'
    id= Column(Integer, primary_key=True)
    name = Column(String(50))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    description = Column(String(500))
    dimensions = Column(Float)
    specie_id = Column(Integer, ForeignKey('species.id'))
    character_specie = relationship(Species)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    character_gender = relationship(Gender)
    affiliation_id = Column(Integer, ForeignKey('affiliation.id'))
    character_affiliation = relationship(Affiliation)

    
class Creatures(Base):
    __tablename__ ='creatures'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    dimensions = Column(Float)

class Vehicles(Base):
    __tablename__='vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    dimensions = Column(Float)
    affiliation_id = Column(Integer, ForeignKey('affiliation.id'))
    character_affiliation = relationship(Affiliation)

class Droids(Base):
    __tablename__='droids'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))

class Weapons(Base):
    __tablename__='weapons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class FavoritePlanet(Base):
    __tablename__='favorite_planets'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)
    

class FavoriteFilm(Base):
    __tablename__ = 'favorite_films'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class FavoriteCreatures(Base):
    __tablename__ = 'favorite_creatures'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    creature_id = Column(Integer, ForeignKey('creatures.id'), primary_key=True)

class FavoriteVehicles(Base):
    __tablename__ = 'favorite_vehicles'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)

class FavoriteDroids(Base):
    __tablename__ = 'favorite_droids'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    droids_id = Column(Integer, ForeignKey('droids.id'), primary_key=True)

class FavoriteWeapons(Base):
    __tablename__ = 'favorite_weapons'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    weapons_id = Column(Integer, ForeignKey('weapons.id'), primary_key=True)


   


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
