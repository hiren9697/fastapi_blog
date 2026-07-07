from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class= HTMLResponse)
@app.get("/posts", response_class= HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

posts: list[dict] = [
    {"id": 1, "author": "Hirenkumar", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"},
    {"id": 2, "author": "John", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"}
]

@app.get("/api/posts")
def get_posts():
    return posts
