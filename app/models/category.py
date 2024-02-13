from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'category'

    catnum = Column(Integer, primary_key=True, autoincrement=True)
    catname = Column(String(18), nullable=False)
    catcod = Column(Integer, nullable=False)    # 240213 issue: 중복 불가 나중에 추가
    catcodref = Column(Integer, default=None)
    regdate = Column(DateTime, default=datetime.now)
