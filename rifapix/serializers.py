from datetime import datetime
from fastapi import HTTPException, status
from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    user: str
    name: str
    password: str
    email: str
    active: bool

class UserIn(BaseModel):
    user: str
    name: str
    password: str
    email: str

class RifaOut(BaseModel):
    id: int
    user_id: int
    quantity: int
    value: float
    pix_key: str
    title: str
    description: str
    award: str
    date_start: datetime
    date_finish: datetime

class RifaIn(BaseModel):
    user_id: int
    quantity: int
    value: float
    pix_key: str
    title: str
    description: str
    award: str
    date_start: datetime
    date_finish: datetime