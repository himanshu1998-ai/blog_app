import os
import requests
from fastapi import APIRouter, Request, status, Response, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.exc import IntegrityError
from blog.entrypoint.postgresql.database import get_db
from blog.entrypoint.postgresql.models import Blog
from blog.repository.impl.repo_store import REPOSTORE
from blog.usecases.read.listallblog import LISTALLBLOGUSECASE
from blog.entrypoint.routers.blog_route import listall_blog
from sqlalchemy.orm import Session
router = APIRouter()

CONFIG_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(CONFIG_PATH, "./templates"))

templates = Jinja2Templates(directory=TEMPLATE_PATH)


@router.get("/", status_code=200, response_class=HTMLResponse)
async def home_page(request: Request, msg: str = None):

    repo = REPOSTORE(next(get_db()))
    usecase = LISTALLBLOGUSECASE(repo)
    blogs = usecase.execute()


    # url = f'http://127.0.0.1:5005/listall_blog'
    # user_detail = requests.get(url)
    # blogs = user_detail.json()

    return templates.TemplateResponse('index.html', {'request': request, "blogs": blogs, "msg": msg})


@router.get("/detail/{blog_id}", status_code=200, response_class=HTMLResponse)
async def detail_page(request: Request, blog_id: int):
    url_read_blog = f'http://0.0.0.0:5005/read_blog?blog_id={blog_id}'
    read_blog = requests.get(url_read_blog)
    blog = read_blog.json()

    url = f'http://0.0.0.0:5005/get_user?user_id={blog["user_id"]}'
    user_detail = requests.get(url)
    owner = user_detail.json()

    return templates.TemplateResponse('detail.html', {'request': request, "blog": blog, "owner": owner})


@router.get("/register", status_code=200, response_class=HTMLResponse)
def registeration(request: Request):

    return templates.TemplateResponse('register.html', {'request': request})


@router.post("/register", status_code=200, response_class=HTMLResponse)
async def registeration(request: Request):
    form = await request.form()
    user_name = form.get('username')
    email = form.get('email')
    password = form.get('password')
    errors = []
    if len(password) < 4:
        errors.append("Password should be atleast 4 Charater long ")
    params = {"name": user_name, "email": email, "password": password}
    url = f'http://0.0.0.0:5005/create_user'
    try:
        requests.post(url, params=params)

        return RedirectResponse("/?msg=Successfully Registered", status_code=status.HTTP_302_FOUND)
    except IntegrityError:
        errors.append("Email already Exists!!")
        return templates.TemplateResponse('register.html', {'request': request, "errors": errors})


@router.get("/login", status_code=200, response_class=HTMLResponse)
def login(request: Request):

    return templates.TemplateResponse('login.html', {'request': request})


@router.post("/login", status_code=200, response_class=HTMLResponse)
async def login(response: Response, request: Request):
    form = await request.form()
    email = form.get('email')
    password = form.get('password')

    errors = []

    url = 'http://0.0.0.0:5005/login'
    user_detail = {'username': email, 'password': password}

    try:

        res = requests.post(url, data=user_detail)
        if not res:
            errors.append("Email or password Incorrect")
            return templates.TemplateResponse('login.html', {'request': request, "errors": errors})
        data = res.json()

        msg = "Login Success"
        response = templates.TemplateResponse('login.html', {'request': request, "msg": msg})
        response.set_cookie(key="access_token", value=data["access_token"], httponly=True)
        return response
    except:
        errors.append("Something Wrong!!")
        return templates.TemplateResponse('login.html', {'request': request})
