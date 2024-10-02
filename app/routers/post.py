from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from typing import List

from app.contracts import CreatePost, PostResponse
from app import models
from app.database import get_db
from app.oauth2 import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(
    post: CreatePost,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
):
    # cursor.execute('"INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *"', (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", response_model=PostResponse)
def get_post(
    id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)
):
    # cursor.execute('"SELECT * FROM posts WHERE id = %s"', (str(id),))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exit",
        )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)
):
    # cursor.execute('"DELETE FROM posts WHERE id = %s"', (str(id),))
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exit",
        )
    db.delete(post)
    db.commit()
    return


@router.put("/{id}", response_model=PostResponse)
def update_post(
    id: int,
    update_post: CreatePost,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
):
    # cursor.execute('"UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s" RETURNING *"', (post.title, post.content, post.published, str(id)))
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exit",
        )

    post_query.update(update_post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()
