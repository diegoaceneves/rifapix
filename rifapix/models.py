from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    user: str
    password: str
    email: str
    active: bool

class Rifa(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    user_id: int
    quantity: int
    value: float
    pix_key: str
    title: str
    description: str
    award: str
    date_start: datetime
    date_finish: datetime
    active: bool

class Number(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    rifa_id: int
    number: int
    description: str
    date: datetime = Field(default_factory=datetime.now)

    
        



















# class Beer(SQLModel, table=True):
#     id: Optional[int] = Field(primary_key=True, default=None, index=True)
#     name: str
#     style: str
#     flavor: int
#     image: int
#     cost: int
#     rate: int = 0
#     date: datetime = Field(default_factory=datetime.now)

#     # NEW
#     @validator("image", "flavor", "cost")
#     def validate_ratings(cls, v, field):
#         if v < 1 or v > 10:
#             raise RuntimeError(f"{field.name} must be between 1 and 10")
#         return v

#     @validator("rate", always=True)
#     def calculate_rate(cls, v, values):
#         rate = mean([values["flavor"], values["image"], values["cost"]])
#         return int(rate)