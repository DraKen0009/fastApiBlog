from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
from database import get_db
from hashing import Hash
from token import create_access_token

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="No user with this id")

    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=403, detail="Incorrect Password")

    access_token = create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
