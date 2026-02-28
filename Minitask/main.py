from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id:int
    title:str
    completed:bool = False

tasks = []

@app.post('/itemslist')
def items(product: Task):
    tasks.append(product)
    return product

@app.get('/itemslist/{id}')
def idbased(id:int):
    for task in tasks:
        if task.id == id:
            return task
    return {"not fount"}      