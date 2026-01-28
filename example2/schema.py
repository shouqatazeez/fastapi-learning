from pydantic import BaseModel


class Example(BaseModel):
    title:str
    body:str
