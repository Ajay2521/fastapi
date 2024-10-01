from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 
import psycopg2

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool

try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres')
    cursor = conn.cursor()
    print("Database connection was successful!")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)

temp_post = [
   {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2} 
]

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/posts")
def create_post(post: Post):
    temp_post.append(post.dict())
    return {"data": post}

@app.get("/posts/{id}")
def get_post(id: int):
    return {"post_id": id}


@app.get("/posts")
def get_posts():
    return {"data": temp_post}
