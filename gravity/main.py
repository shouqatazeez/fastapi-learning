from fastapi import FastAPI,HTTPException
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

@app.get('/user/{userid}')
def user(userid:str):
    if userid=='admin':
        return {"success": True}
    else:
     raise HTTPException(status_code=404,detail="user not found")

class public_pizza(BaseModel):
    name:str
    price:float

@app.get('/order/{pizza}',response_model=public_pizza)
def pizzadetails(pizza:str):
    kitchen_data = {
      "name":pizza,
      "price":1000,
      'cost_to_make':600,
      'secret_recipe':3
    } 
    return kitchen_data


    