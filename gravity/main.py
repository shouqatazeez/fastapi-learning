from fastapi import FastAPI

app = FastAPI()

@app.get('/status')
def server_status():
    return {"status":"running smoothly"}

@app.get('/users/{username}')
def username(username):
    return  {"greeting": f"Hello, {username}!"}