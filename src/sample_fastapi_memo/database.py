from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from uuid6 import uuid7
from sqlalchemy_utils import UUIDType
from sqlalchemy.types import Text

Base = declarative_base()

engine=create_engine(f"postgresql+psycopg://postgres:postgres@localhost:5432/memo")

def get_db_session() -> scoped_session:
    """ 新しいDBコネクションを返す
    """
    return scoped_session(sessionmaker(bind=engine))

class Memo(Base):
    __tablename__ = "memo"  # テーブル名を指定
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid7)
    memo = Column(Text)

    def memo_result(self):  # メモの内容を返す
        return "{self.id} {self.memo}"
    