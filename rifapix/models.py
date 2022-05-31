from datetime import datetime
from enum import unique
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint, Column, String

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    user: str = Field(sa_column=Column("user", String, unique=True))
    password: str
    email: str = Field(sa_column=Column("email", String, unique=True))
    active: Optional[bool] = Field(default=True)

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
    active: Optional[bool] = Field(default=True)

class Number(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    rifa_id: int
    number: int
    description: str
    date: datetime = Field(default_factory=datetime.now)