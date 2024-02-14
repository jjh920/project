from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Keycat(Base):
    __tablename__ = 'keycat'

    keycatnum = Column(Integer, primary_key=True, autoincrement=True)
    keycatname = Column(String(18), nullable=False)
    subcatnum = Column(Integer, default=0)
