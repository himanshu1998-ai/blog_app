from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from blog.entrypoint.postgresql.database import get_db
from blog.repository.interface.user_repo import IUSERREPO
from blog.entity.user import USER
from blog.entrypoint.postgresql.models import User
from blog.model.schemas import UserSchema
from blog.hashing.hash import bcrypt, verify
from blog.Authentication import token


class USERSTORE(IUSERREPO):

    def __init__(self, db: Session = Depends(get_db)):
        self.session = db

    def prepare_payload(self, payload: User):

        return dict(user_id=payload.id, name=payload.name, email=payload.email, password=payload.password)

    def create_user(self, user: UserSchema) -> USER:
        user = User(name=user.name, email=user.email, password=bcrypt(user.password))
        self.session.add(user)
        self.session.commit()
        return USER.from_json(self.prepare_payload(user))

    def login_user(self, request: OAuth2PasswordRequestForm):
        user = self.session.query(User).filter(User.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the email {request.username} is not found!")
        if not verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Email or Password is wrong")
        access_token = token.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    def get_user(self, user_id: int) -> USER:
        user = self.session.query(User).get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {user_id} is not available")
        return USER.from_json(self.prepare_payload(user))

    def delete_user(self, user_id: int) -> int:
        user = self.session.query(User).filter(User.id == user_id).delete()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {user_id} is not available")
        return user_id
