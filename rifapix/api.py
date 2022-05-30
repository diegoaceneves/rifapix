from typing import List, Optional

from fastapi import FastAPI, Response, status

from rifapix.core import get_rifas_from_database, get_users_from_database
from rifapix.database import get_session
from rifapix.models import User, Rifa, Number
from rifapix.serializers import UserIn, UserOut, RifaIn, RifaOut

api = FastAPI(title="rifapix ")


@api.get("/users", response_model=List[UserOut])
async def list_users():
    """List users from the database"""
    users = get_users_from_database()
    return users


@api.post("/users", response_model=UserOut)
async def add_user(user_in: UserIn, response: Response):
    user = User(**user_in.dict())
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    response.status_code = status.HTTP_201_CREATED
    return user

@api.get("/rifas", response_model=List[RifaOut])
async def list_rifas():
    """List rifas from the database"""
    users = get_rifas_from_database()
    return users


@api.post("/rifas", response_model=RifaOut)
async def add_rifa(rifa_in: RifaIn, response: Response):
    rifa = Rifa(**rifa_in.dict())
    with get_session() as session:
        session.add(rifa)
        session.commit()
        session.refresh(rifa)

    response.status_code = status.HTTP_201_CREATED
    return rifa

     