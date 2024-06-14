from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from typing import Optional


app = FastAPI()

@app.get("/")

def index():
    return {"data": {'name':'Sarthak'}}



@app.get("/blog")
def about(limit=10, published: bool = True, sort: Optional[str]= None):
    if published:
        return {"data": f'{limit} published blogs from the db'}
    else:
        return {"data": f'{limit} blogs from the db'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {'1','2'}}