from fastapi import FastAPI

app = FastAPI()

@app.get('/data')
def name():
    return "hello Bhai"