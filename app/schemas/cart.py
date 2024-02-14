from datetime import datetime

from pydantic import BaseModel


class Cart(BaseModel):
    cartnum: int
    userid: str
    prodnum: int
    quantity: int
    regdate: datetime

    class Config:
        from_attributes = True


class NewCart(BaseModel):
    pass
