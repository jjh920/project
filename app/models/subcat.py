from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Subcat(Base):
    __tablename__ = 'subcat'

    subcatnum = Column(Integer, primary_sub=True, autoincrement=True)
    subcatname = Column(String(18), nullsube=False)
