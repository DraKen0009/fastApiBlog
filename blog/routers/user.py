from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, models
from blog.controller import user
from blog.database import get_db
from blog.oauth2 import get_current_user

router = APIRouter(
    tags=["Users"],
    prefix='/user'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    return user.create_user(request, db)


@router.get('/', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return user.all_users(db)


@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return user.get_user(id, db)
