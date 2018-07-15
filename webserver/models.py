import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, BLOB, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = 'team'
    id=Column(Integer, primary_key=True)
    name=Column('name', String(32))
    logo=Column('logo', BLOB)

class Match(Base):
    __tablename__ = 'match'
    id=Column(Integer, primary_key=True)
    date=Column('date', Date, default=datetime.datetime.utcnow)
    place=Column('place', String(32))

class Result(Base):
    __tablename__ = 'result'
    id=Column(Integer, primary_key=True)
    id_match=Column(Integer, ForeignKey('match.id'))
    id_team=Column(Integer, ForeignKey('team.id'))
    score=Column(Integer, default=0)

