from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


db = []

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published: bool = False


db.append(BlogPost(title="First Post", content="This is my first post", author="John Doe"))

@app.get("/posts", response_model=list[BlogPost])
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
    delete_post = db[post_id - 1]
    return delete_post
