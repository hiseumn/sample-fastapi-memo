from sqlalchemy import desc
from sqlalchemy.orm import scoped_session
from database import Memo
from schemas import InputMemo as InputMemoSchema, Memo as MemoSchema
from uuid6 import uuid7

def add_memo(memo: InputMemoSchema, session: scoped_session) -> Memo | None:
    memo = Memo(id=uuid7(), memo=memo.memo)
    session.add(memo)
    session.commit()
    session.refresh(memo)
    return memo


def get_memo(session: scoped_session):
    return session.query(Memo).order_by(desc('id')).limit(20).all()
