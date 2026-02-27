from fastapi import FastAPI

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
