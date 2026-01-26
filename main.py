from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
def intro():

    return {'data': {
        'name': "shouqat"
    }}


@app.get('/blogs/unpublished')
def unpublished():
    return {'data': "unpublisedblogs"}


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
