from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import scoped_session
from . import functions
from .database import get_db_session
from .schemas import Memo

router = APIRouter()


@router.get("/memo", tags=["/memo"])
def get_memo(session: scoped_session = Depends(get_db_session)) -> list[Memo]:
    memo = functions.get_memo(session)
    return list(map(Memo.model_validate, memo))


@router.post("/memo", tags=["/memo"])
def add_memo(name: str, author_id: int, session: scoped_session = Depends(get_db_session)) -> Memo:
    memo = functions.add_memo(memo, session)
    return Memo.model_validate(memo)
