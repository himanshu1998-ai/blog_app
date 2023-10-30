from fastapi import APIRouter, Depends
from blog.Authentication import oAuth
from blog.repository.impl.repo_store import REPOSTORE
from blog.usecases.create.create_blog import CREATEBLOGUSECASE
from blog.usecases.read.read_blog import READBLOGUSECASE
from blog.usecases.read.listall import LISTBLOGUSECASE
from blog.usecases.read.listallblog import LISTALLBLOGUSECASE
from blog.usecases.delete.delete_blog import DELETEBLOGUSECASE
from blog.usecases.update.update_blog import UPDATEBLOGUSECASE
from blog.model.schemas import BlogSchema, UserSchema
from blog.entrypoint.postgresql.database import get_db
from blog.entrypoint.routers import config

router = APIRouter()


@router.post(config.CREATE_BLOG, tags=['blogs'])
def create_blog(title: str, description: str, user_id: int, current_user: UserSchema = Depends(oAuth.get_current_user)):
    user = current_user
    repo = REPOSTORE(next(get_db()))
    usecase = CREATEBLOGUSECASE(repo)
    obj = BlogSchema(title=title, description=description, user_id=user_id)
    data = usecase.execute(model=obj)
    return data


@router.get(config.READ_BLOG, tags=['blogs'])
def read_blog(blog_id: int):

    repo = REPOSTORE(next(get_db()))
    usecase = READBLOGUSECASE(repo)
    data = usecase.execute(blog_id=blog_id)
    return data


@router.get(config.LIST_BLOG, tags=['blogs'])
def list_blog(user_id: int):

    repo = REPOSTORE(next(get_db()))
    usecase = LISTBLOGUSECASE(repo)
    data = usecase.execute(user_id=user_id)
    return data


@router.get(config.LISTALL_BLOG, tags=['blogs'])
def listall_blog():

    repo = REPOSTORE(next(get_db()))
    usecase = LISTALLBLOGUSECASE(repo)
    data = usecase.execute()
    return data


@router.delete(config.DELETE_BLOG, tags=['blogs'])
def delete_blog(blog_id: int, current_user: UserSchema = Depends(oAuth.get_current_user)):
    user = current_user
    repo = REPOSTORE(next(get_db()))
    usecase = DELETEBLOGUSECASE(repo)
    data = usecase.execute(blog_id=blog_id)
    return data


@router.put(config.UPDATE_BLOG, tags=['blogs'])
def update_blog(blog_id: int, current_user: UserSchema = Depends(oAuth.get_current_user)):
    user = current_user
    repo = REPOSTORE(next(get_db()))
    usecase = UPDATEBLOGUSECASE(repo)
    data = usecase.execute(blog_id=blog_id)
    return data
