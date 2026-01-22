from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
def intro():

    return {'data': {
        'name': "shouqat"
    }}


@app.get('/blogs/unpubliched')
def unpubliched():
    return {'data': "unpublicedblogs"}


@app.get('/blogs/{id}')
def aboutpage(id: int):
    return {
        'data': {
            id
        }
    }


@app.get('/blogs/{id}/comments')
def blogcomment(id):
    return {
        'data': {
            '1',
            '2'
        }
    }
