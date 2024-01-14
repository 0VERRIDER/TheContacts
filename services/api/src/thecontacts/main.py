from typing import Union
from time import sleep

from fastapi import FastAPI
from .data.database.db import engine, Base

# Routes
from .routes.users.create import router as user_create_router

app = FastAPI(
    title="The Contacts API",
    description="A contact importer and management api.",
    version="0.0.1",
    docs_url="/",
)

# create database tables
Base.metadata.create_all(bind=engine)


# User routes
# User create
app.include_router(
    user_create_router,
    prefix="/signup",
    tags=["users"],
)