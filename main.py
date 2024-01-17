from fastapi import FastAPI

import models
from database import engine
from routers import blog, authentication, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
