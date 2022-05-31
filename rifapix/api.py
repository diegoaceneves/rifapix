from datetime import datetime
from itertools import starmap
from fastapi import FastAPI, Response, status
from typing import List, Optional
from sqlmodel import select

from rifapix.core import get_users_from_database, get_rifas_from_database
from rifapix.database import get_session
from rifapix.models import User, Rifa, Number
from rifapix.serializers import UserIn, UserOut, RifaIn, RifaOut

api = FastAPI(
    title="rifapix ",
    version="v0.0.1"
    )

@api.get("/users", response_model=List[UserOut])
async def  list_users(response: Response, id: Optional[int] = None):
    """List users from the database"""
    with get_session() as session:
        sql = select(User)
        if id:
            sql = sql.where(User.id == id)

        if list(session.exec(sql)):
            response.status_code = status.HTTP_200_OK
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
        return list(session.exec(sql))

@api.post("/users", response_model=UserOut)
async def add_user(user_in: UserIn, response: Response):
    """Add user to database"""
    user = User(**user_in.dict())
    with get_session() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            response.status_code = status.HTTP_201_CREATED
        except:
            response.status_code = status.HTTP_400_BAD_REQUEST
        return user

@api.delete("/users", response_model=UserOut)
async def  delete_users(response: Response, id: Optional[int] = None):
    """Delete users from the database"""
    if id:
        user=get_users_from_database(id=id)
        if user:
            with get_session() as session:
                session.delete(user[0])
                session.commit()
                response.status_code=status.HTTP_200_OK
                return user[0]
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code=status.HTTP_400_BAD_REQUEST
    return "[]"
    

@api.get("/rifas", response_model=List[RifaOut])
async def  list_rifas(response: Response, id: Optional[int] = None):
    """List rifas from the database"""
    with get_session() as session:
        sql = select(Rifa)
        if id:
            sql = sql.where(Rifa.id == id)

        if list(session.exec(sql)):
            response.status_code = status.HTTP_200_OK
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
        return list(session.exec(sql))

@api.post("/rifas", response_model=RifaOut)
async def add_rifa(rifa_in: RifaIn, response: Response):
    """Add Rifa to database"""
    rifa = Rifa(**rifa_in.dict())
    with get_session() as session:
        try:
            session.add(rifa)
            session.commit()
            session.refresh(rifa)
            response.status_code = status.HTTP_201_CREATED
        except:
            response.status_code = status.HTTP_400_BAD_REQUEST
        return rifa

@api.delete("/rifas", response_model=RifaOut)
async def  delete_rifas(response: Response, id: Optional[int] = None):
    """Delete Rifas from the database"""
    if id:
        rifa=get_rifas_from_database(id=id)
        if rifa:
            with get_session() as session:
                session.delete(rifa[0])
                session.commit()
                response.status_code=status.HTTP_200_OK
                return rifa[0]
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code=status.HTTP_400_BAD_REQUEST
    return "[]"        