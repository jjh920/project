from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = 'order'

    ordernum = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(18), nullable=False)
    quantity = Column(Integer, default=0)
    regdate = Column(DateTime, default=datetime.now)
    prodnum = Column(Integer, default=0)
