from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

import models
from database import engine, sessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    name:str
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

@app.get('/products')
def list_of_products(category:str=None, max_price:int=100, on_sale:bool=False):
    return{"productcategory":category, "productprice":max_price, "status":on_sale}

class user(BaseModel):
    username:str = Field(..., min_length =3, max_length=15)
    age:int = Field(..., gt=0, lt=120)
@app.post('/userdetails')
def details(model:user):
    return{
       "message":'user created successfully',"data":model
    }

class student_details(BaseModel):
    street:str
    town:str
    doorno:int

class student(BaseModel):
    name:str = Field(..., min_length=3, max_length=15)
    age:int = Field(..., gt=0, lt=30)
    id:int = Field(..., gt=10, lt=12)

    studentdetails:student_details  

@app.post('/registry')
def registry_student(data:student):
    return{
        "message":"student registry perfectely",
         "data": data
    }

@app.post('/db_register')
def create_db_user(user:UserProfile, db:Session= Depends(get_db)):

    new_db_user = models.User(email=user.email, name=user.name)

    db.add(new_db_user)

    db.commit()

    db.refresh(new_db_user)

    return{'message':'saved to database', "user":new_db_user}