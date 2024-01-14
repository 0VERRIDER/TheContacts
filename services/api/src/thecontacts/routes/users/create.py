from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from ...data.database.db import get_db
from ...repositories.UserRepository import UserRepository
from ...schemas.user import UserCreate as UserCreateSchema

router = APIRouter()


@router.post("/", tags=["users", "signup"], response_model=UserCreateSchema)
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    return await UserRepository.create_user( db = db, user = user)