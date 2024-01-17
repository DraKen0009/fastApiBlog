from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import schemas
import models
from controller import blog
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def show_blogs(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return blog.get_blog(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def show_blog(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db)
