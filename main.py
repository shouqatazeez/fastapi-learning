from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
def intro(limit):
# This is the example of the query parameter
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


