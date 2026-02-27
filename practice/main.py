from fastapi import FastAPI

app = FastAPI()

@app.get('/data')
def name():
    return "hello Bhai"

@app.get('/data/{name}')
def name(name:str):
    return f"Assamualikm {name}"