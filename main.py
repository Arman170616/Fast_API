from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Mock data to simulate a database
db = []

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published: bool = False

# Example initial data
db.append(BlogPost(title="First Post", content="Hello, world!", author="John Doe"))

@app.get("/posts", response_model=List[BlogPost])
def get_posts():
    return db

@app.get("/posts/{post_id}", response_model=BlogPost)
def get_post(post_id: int):
    return db[post_id - 1]

@app.post("/posts", response_model=BlogPost)
def create_post(post: BlogPost):
    db.append(post)
    return post

@app.put("/posts/{post_id}", response_model=BlogPost)
def update_post(post_id: int, post: BlogPost):
    db[post_id - 1] = post
    return post

@app.delete("/posts/{post_id}", response_model=BlogPost)
def delete_post(post_id: int):
    deleted_post = db.pop(post_id - 1)
    return deleted_post






"""
Use HTTP methods (GET, POST, PUT, DELETE) on the endpoints:
GET /posts: Get all posts
GET /posts/{post_id}: Get a specific post
POST /posts: Create a new post
PUT /posts/{post_id}: Update a post
DELETE /posts/{post_id}: Delete a post

"""