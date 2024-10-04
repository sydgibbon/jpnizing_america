from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, default=False)

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    access_level = Column(Integer, nullable=False)

class Level(Base):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True)
    level = Column(String(10), nullable=False)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    video_url = Column(String(200), nullable=False)
    level_id = Column(Integer, ForeignKey('levels.id', ondelete='CASCADE'))

class UserLevel(Base):
    __tablename__ = 'user_levels'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    level_id = Column(Integer, ForeignKey('levels.id', ondelete='CASCADE'), primary_key=True)
    access_granted = Column(Boolean, default=True)
