from fastapi import FastAPI
from schema import blog
app = FastAPI()



@app.post('/blog')
def create_element(storedata:blog):
    return storedata
    

