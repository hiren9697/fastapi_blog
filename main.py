from fastapi import HTTPException, status
from schemas import PostResponse
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# MARK: - Mock Data
posts: list[dict] = [
    {"id": 1, "author": "Hirenkumar", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"},
    {"id": 2, "author": "John", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"}
]

app = FastAPI()

# MARK: - API Endpoints
@app.get("/", response_class= HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class= HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts

@app.get("/post/{post_id}")
def post_page(post_id: int):
    for post in posts: 
        if post['id'] == post_id:
            return post 
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")