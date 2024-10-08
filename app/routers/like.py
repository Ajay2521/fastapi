from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from app.contracts import Like
from app import models, oauth2
from app.database import get_db
from app.routers.user import create_user
from app.oauth2 import get_current_user


router = APIRouter(prefix="/like", tags=["Like"])


@router.post("", status_code=status.HTTP_201_CREATED)
def like(
    like: Like, db: Session = Depends(get_db), create_user=Depends(get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {like.post_id} does not exit",
        )

    like_query = db.query(models.Like).filter(
        models.Like.post_id == like.post_id, models.Like.user_id == create_user.id
    )

    if like_query.first():
        like_query.delete(synchronize_session=False)
        db.commit()
    else:
        new_like = models.Like(post_id=like.post_id, user_id=create_user.id)
        db.add(new_like)
        db.commit()
