from fastapi import APIRouter, Depends
from blog.repository.impl.user_store import USERSTORE
from blog.usecases.create.create_user import CREATEUSERUSECASE
from blog.usecases.read.login_user import LOGINUSERUSECASE
from blog.usecases.read.get_user import GETUSERUSECASE
from blog.usecases.delete.delete_user import DELETEUSERUSECASE
from blog.model.schemas import UserSchema, ShowUser
from blog.entrypoint.postgresql.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from blog.entrypoint.routers import config

router = APIRouter()


@router.post(config.CREATE_USER, tags=['users'])
def create_user(name: str, email: str, password: str):
    repo = USERSTORE(next(get_db()))
    usecase = CREATEUSERUSECASE(repo)
    obj = UserSchema(name=name, email=email, password=password)
    data = usecase.execute(model=obj)
    return data


@router.post(config.LOGIN, tags=['users'])
async def login_user(formdata: OAuth2PasswordRequestForm = Depends()):
    repo = USERSTORE(next(get_db()))
    usecase = LOGINUSERUSECASE(repo)

    data = usecase.execute(formdata)
    return data


@router.get(config.GET_USER, response_model=ShowUser, tags=['users'])
def get_user(user_id: int):
    repo = USERSTORE(next(get_db()))
    usecase = GETUSERUSECASE(repo)
    data = usecase.execute(user_id=user_id)
    return data


@router.delete(config.DELETE_USER, tags=['users'])
def delete_user(user_id: int):
    repo = USERSTORE(next(get_db()))
    usecase = DELETEUSERUSECASE(repo)
    data = usecase.execute(user_id=user_id)
    return data

