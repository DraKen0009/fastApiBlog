from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


def update_blog(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog doesn't exist")

    blog.title = request.title
    blog.body = request.body if request.body else blog.body

    db.commit()

    return "updated blog successfully"


def delete_blog(id: int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted"}


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
