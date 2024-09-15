from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import random

app = FastAPI()

# Here app is a decorator
 
@app.get("/")
def root1():
    return {"message": "Hello"}

@app.get("/")  # Same Router 
def root2():
    return {"message": "Hello 2"}

# Router '/' --> First


post_list = [{
    "id": "1",
    "title": "My first post",
    "content": "This is my first post"
},
{
    "id": "2",
    "title": "My second post",
    "content": "This is my second post"
},
{
    "id": "3",
    "title": "My third post",
    "content": "This is my third post"
}
]


def addPost(post):
    post_list.append(post)
    return


# GET ALL POST
@app.get("/getAllposts")
def getpost():
    return {"post": post_list}

# Post API
class Post(BaseModel):
    title: str
    content: str
# CREATE POST
@app.post("/create-post")
def createPost(payload: Post):   
    new_post = payload.dict() 
    new_post['id'] = str(random.randint(0, 1000))
    addPost(new_post)
    return {"message": "Post created successfully"}

# Schema for Request
# class Post(BaseModel):
#     title: str
#     content: str

# @app.post("/new-post")
# def newPost(post:Post):
#     print(post)
#     return {"new-post": "created"}  