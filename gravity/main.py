from fastapi import FastAPI

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