from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
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


