from datetime import datetime
from itertools import starmap
from typing import List, Optional
from sqlmodel import select
from rifapix.database import get_session
from rifapix.models import User, Rifa, Number

def add_user_to_database(
    user: str,
    password: str,
    email: str,
    active: bool
) -> bool:
    with get_session() as session:
        user = User(**locals())
        session.add(user)
        session.commit()
    return True

def get_users_from_database() -> List[User]:
    with get_session() as session:
        sql = select(User)
        return list(session.exec(sql))    

def add_rifas_to_database(
    user_id: int,
    quantity: int,
    value: float,
    pix_key: str,
    title: str,
    description: str,
    award: str,
    date_start: datetime,
    date_finish: datetime,
    active: bool   
) -> bool:
    with get_session() as session:
        rifa = Rifa(**locals())
        session.add(rifa)
        session.commit()
    return True

def get_rifas_from_database() -> List[Rifa]:
    with get_session() as session:
        sql = select(Rifa)
        return list(session.exec(sql))
    

def add_number_to_database(
    rifa_id: int,
    number: int,
    description: str
) -> bool:
    with get_session() as session:
        number = Number(**locals())
        session.add(number)
        session.commit()

    return True




# def get_beers_from_database(style: Optional[str] = None) -> List[Beer]:
#     with get_session() as session:
#         sql = select(Beer)
#         if style:
#             sql = sql.where(Beer.style == style)
#         return list(session.exec(sql))