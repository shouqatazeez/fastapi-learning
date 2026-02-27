from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id:int
    title:str
    completed:bool = False

tasks = []

@app.post('/itemslist')
def items(product:Task):
    tasks.append(product)
    return tasks
