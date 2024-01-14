from sqlalchemy.orm import Session

from ..models.user import Users as UserModel
from ..schemas.user import UserCreate as UserCreateSchema

class UserRepository:
    async def create_user(db: Session, user: UserCreateSchema):
        db_user = UserModel(
            name=user.name,
            phone=user.phone,
            password=user.password,
            email=user.email,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user