from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

# Here app is a decorator
 
@app.get("/")
def root1():
    return {"message": "Hello"}

@app.get("/")  # Same Router 
def root2():
    return {"message": "Hello 2"}

# Router '/' --> First

@app.get("/get-post")
def getpost():
    return {"message": "Get Post"}

# Post API
@app.post("/create-post")
def createPost(payload: dict = Body(...)):
    print(payload)
    return {"create-post": payload}

# Schema for Request
class Post(BaseModel):

    title: str
    content: str

@app.post("/new-post")
def newPost(post:Post):
    print(post)
    return {"new-post": "created"}