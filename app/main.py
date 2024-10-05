from fastapi import FastAPI

from app.routers import auth, post, user, like

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(like.router)


@app.get("/ping")
def ping():
    return {"message": "pong"}
