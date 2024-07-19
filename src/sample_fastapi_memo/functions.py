from sqlalchemy import select
from sqlalchemy.orm import scoped_session
from .database import Memo
from uuid6 import uuid7

def add_memo(memo: str, session: scoped_session) -> Memo | None:
    memo = Memo(id=uuid7(), memo=memo)
    session.add(memo)
    session.commit()
    session.refresh(memo)
    return memo


def get_memo(session: scoped_session):
    return session.scalars(select(Memo))
