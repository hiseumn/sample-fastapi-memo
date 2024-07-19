from pydantic import BaseModel, ConfigDict


class Memo(BaseModel):
    id: int
    memo: str

    model_config = ConfigDict(from_attributes=True)
