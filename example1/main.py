from fastapi import FastAPI
# This is how we import BaseModel for the purpose of the post the data into the database
from pydantic import BaseModel

#This is how we import Optinal from the typing
from typing import Optional

app = FastAPI()


@app.get('/')
# This is the example of the query parameter 
# http://127.0.0.1:8000/blogs?limit=10$=&published=True
def intro(limit=10, published:bool = True ):
    if published:
        return{
            'data':f'The {limit} Published blocks from the database'
        }
    else:
        return{
        'data':f'The {limit} blocks from the database'
         }

  

@app.get('/blogs/unpublished')
def unpublished():
    return {'data': "unpublisdblogs"}


@app.get('/blogs/{id}')
def aboutpage(id: int):
    return {
        'data': {
            id
        }
    }


@app.get('/blogs/{id}/comments')
def blogcomment(id:str):
    return {
        'data': {
            '1',
            '2'
        }
    }


#This is how we create the post method and use it 

class Model (BaseModel):
    title:str
    body:str
    published:Optional[bool]



@app.post('/blogs')
def blogpost(request:Model):
    return{f'blog is created with the {request.title}'}
    

