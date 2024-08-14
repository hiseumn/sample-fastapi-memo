from uuid import UUID
from pydantic import BaseModel, ConfigDict


class InputMemo(BaseModel):
    memo: str
    model_config = ConfigDict(from_attributes=True)


class Memo(InputMemo):
    id: UUID