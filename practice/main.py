from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/data')
def name():
    return "hello Bhai"

@app.get('/data/{name}')
def name(name:str):
    return f"Assalmualikm {name}"


@app.get('/search')
def products(name:str, price:int):
    return {"product":name,"productprice":price}

class products(BaseModel):
    name:str
    price:int

@app.post('/product')
def list(product:products):
    return{
        "Item name":product.name,
        "pricetag":product.price

    }