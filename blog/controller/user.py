from fastapi import HTTPException
from sqlalchemy.orm import Session

from blog import schemas, models
from blog.hashing import Hash


def create_user(request: schemas.User, db: Session):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def all_users(db: Session):
    users = db.query(models.User).all()
    return users


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="No user with this id")

    return user
