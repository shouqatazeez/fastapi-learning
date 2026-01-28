from fastapi import FastAPI
from schema import Example


app = FastAPI()


@app.post('/hello')
def create(request:Example):
    return request