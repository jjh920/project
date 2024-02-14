from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Cart(Base):
    __tablename__ = 'cart'

    cartnum = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(18), nullable=False)
    prodnum = Column(Integer, default=0)
    quantity = Column(Integer, default=0)
    regdate = Column(DateTime, default=datetime.now)
