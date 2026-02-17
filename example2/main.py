from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class blog(BaseModel):
    name:str
    body:str

@app.post('/blog')
def create_element(storedata:blog):
    return storedata
    

