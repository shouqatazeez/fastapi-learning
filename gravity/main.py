from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/status')
def server_status():
    return {"status":"running smoothly"}

@app.get('/users/{username}')
def username(username):
    return  {"greeting": f"Hello, {username}!"}

@app.get('/search')
def search_database(keyword:str, limit:int):
    return {"search_result": f'Searching for the keyword:{keyword} and  showing {limit} results.'}

class UserProfile(BaseModel):
    email:str
    age:int
@app.post('/register')
def register(user_data:UserProfile):
    return {"success":True,
    "registered_user":user_data.email,
    "user_age":user_data.age}






    