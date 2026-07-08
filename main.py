from schemas import PostResponse
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class= HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class= HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

posts: list[dict] = [
    {"id": 1, "author": "Hirenkumar", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"},
    {"id": 2, "author": "John", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"}
]

@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts
