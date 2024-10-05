from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, post, user, like

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(like.router)


@app.get("/ping")
def ping():
    return {"message": "pong"}
