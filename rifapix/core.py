from datetime import datetime
from itertools import starmap
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import FastAPI, Response, status

from rifapix.database import get_session
from rifapix.models import User, Rifa, Number

def add_user_to_database(user: str, password: str, email: str) -> List[User]:
    with get_session() as session:
        userx = User(**locals())
        session.add(userx)
        session.commit()
        
    return list(userx)


def get_users_from_database(id: Optional[int] = None) -> List[User]:
    with get_session() as session:
        sql = select(User)
        if id:
            sql = sql.where(User.id == id)
        return list(session.exec(sql))
        

def del_users_from_database(id: Optional[int] = None) -> List[User]:
    if id:
        user=get_users_from_database(id=id)
        if user:
            with get_session() as session:
                session.delete(user[0])
                session.commit()
                return user[0]
    else:
        return "[]"

    
def add_rifas_to_database(
    user_id: int,
    quantity: int,
    value: float,
    pix_key: str,
    title: str,
    description: str,
    award: str,
    date_start: datetime,
    date_finish: datetime
)  -> List[Rifa]:
    with get_session() as session:
        rifa = Rifa(**locals())
        session.add(rifa)
        session.commit()
    return list(rifa)

def get_rifas_from_database(id: Optional[int] = None) -> List[Rifa]:
    with get_session() as session:
        sql = select(Rifa)
        if id:
            sql = sql.where(Rifa.id == id)
        return list(session.exec(sql))

def del_rifas_from_database(id: Optional[int] = None) -> List[Rifa]:
    if id:
        rifa=get_rifas_from_database(id=id)
        if rifa:
            with get_session() as session:
                session.delete(rifa[0])
                session.commit()
                return rifa[0]
    else:
        return "[]"