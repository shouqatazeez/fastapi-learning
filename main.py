from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def intro():

    return {'data': {
        'name': "shouqat"
    }}


@app.get('/about')
def aboutpage():
    return {
        'data': {
            'aboutpage'
        }
    }
