
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    favorites = relationship('Favorites', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    favorites = relationship('Favorites', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    favorites = relationship('Favorites', back_populates='planet')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    favorites = relationship('Favorites', back_populates='vehicle')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship_id = Column(Integer, ForeignKey('vehicle.id'))
    favorite_type = Column(String, nullable=False)
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites', uselist=False)
    planet = relationship('Planet', back_populates='favorites', uselist=False)
    vehicle = relationship('Vehicle', back_populates='favorites', uselist=False)

render_er(Base, 'diagram.png')




