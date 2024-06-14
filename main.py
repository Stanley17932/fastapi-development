from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI()

@app.get("/")

def index():
    return {"data": {'name':'Sarthak'}}



@app.get("/about")
def about():
    return {"data": "About page"}


@app.get("/blog/id")
def show():
    return {"data": "Blog page"}