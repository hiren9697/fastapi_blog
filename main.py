from fastapi.responses import JSONResponse
from fastapi import HTTPException, Request, status
from schemas import PostResponse, PostCreate
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarlettedHTTPException

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

@app.get("/api/post/{post_id}")
def post_page(post_id: int):
    for post in posts: 
        if post['id'] == post_id:
            return post 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")

@app.post("/api/posts", response_model=PostResponse, status_code=   status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "author": post.author,
        "title": post.title,
        "content": post.content,
        "date_posted": "April 23, 2025",
    }
    posts.append(new_post)
    return new_post

# MARK: - Exception Handlers
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, content={"detail": exception.errors()})

@app.exception_handler(StarlettedHTTPException) 
def general_http_exception_handler(request: Request, exception: StarlettedHTTPException): 
    message = (exception.detail
     if exception.detail
     else "An error occured, please check your request and try again")
    return JSONResponse(status_code=exception.status_code, content={"detail": message})