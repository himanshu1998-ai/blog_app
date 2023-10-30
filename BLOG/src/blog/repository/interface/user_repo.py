from fastapi.security import OAuth2PasswordRequestForm
from abc import ABC, abstractmethod
from blog.entity.user import USER
from blog.model.schemas import UserSchema


class IUSERREPO(ABC):

    @abstractmethod
    def create_user(self, user: UserSchema) -> USER:
        pass

    @abstractmethod
    def login_user(self, request: OAuth2PasswordRequestForm):
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> USER:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> int:
        pass

