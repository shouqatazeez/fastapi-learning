from fastapi import FastAPI

app = FastAPI()

@app.post('/')

def create(title, body):
    return {'title':title, 'body':body}