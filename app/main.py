from fastapi import Depends, FastAPI

from . import models
from app.database import engine
from app.routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connected Successfully")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.Sleep(5)

app.include_router(post.router)
app.include_router(user.router)


@app.get("/ping")
def ping():
    return {"message": "pong"}
