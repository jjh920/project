from datetime import datetime

from pydantic import BaseModel


class Order(BaseModel):
    ordernum: int
    userid: str
    prodnum: int
    quantity: int
    regdate: datetime

    class Config:
        from_attributes = True


class NewOrder(BaseModel):
    pass
