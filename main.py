from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Blog! edit"}

posts: list[dict] = [
    {"id": 1, "author": "Hirenkumar", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"},
    {"id": 2, "author": "John", "title": "Fast API", "content": "This is awsome", "date_posted": "2022"}
]

@app.get("/api/posts")
def get_posts():
    return posts
