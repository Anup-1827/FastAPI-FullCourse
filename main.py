from fastapi import FastAPI, HTTPException, status
from typing import Optional
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
    "id": 1,
    "title": "My first post",
    "content": "This is my first post"
},
{
    "id": 2,
    "title": "My second post",
    "content": "This is my second post"
},
{
    "id": 3,
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
    rating: Optional[int] = None
# CREATE POST
@app.post("/create-post", status_code=status.HTTP_201_CREATED)
def createPost(payload: Post):   
    new_post = payload.dict() 
    new_post['id'] = random.randint(0, 1000)
    addPost(new_post)
    return {"message": "Post created successfully"}


def find_post_by_id( postList,id: int):
    for post in postList:
        if(post["id"] == id):
            return post
    return None

@app.get("/post/{id}")
def getPost(id: int):
    post =  find_post_by_id(post_list, id)
    if post:
        return {"post": post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Post Available")


@app.delete("/posts/{id}")
def deletePost(id: int):
    global post_list
    print(post_list)    
    filtered_post_list = [post for post in post_list if post["id"] != id]
    # print(filtered_post_list)
    post_list =  filtered_post_list
    return {"message":"Deleted Successfully!!"}
