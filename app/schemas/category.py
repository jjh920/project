from datetime import datetime

from pydantic import BaseModel


class Category(BaseModel):
    catnum: int
    catname: str
    catcod: int
    catcoderef: int
    regdate: datetime

    class Config:
        from_attributes = True


class NewCategory(BaseModel):
    catname: str
    catcod: int
    catcoderef: int