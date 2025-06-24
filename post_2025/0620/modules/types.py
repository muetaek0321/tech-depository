from pydantic import BaseModel


__all__ = ["Text"]


class Text(BaseModel):
    text: str

