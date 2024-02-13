from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'product'

    prodnum = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(18), nullable=False)
    exp = Column(String(50), default=None)
    detail = Column(String(500), default=None)
    retail = Column(Integer, nullable=False)
    price = Column(Integer, default=0)
    pctoff = Column(Integer, nullable=False)
    useyn = Column(String(18), nullable=False)
    tumbimg = Column(String(50), nullable=False)
    regdate = Column(DateTime, default=datetime.now)
    catnum = Column(Integer, default=0)
