from typing import Union, List
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status

from blog.entrypoint.postgresql.database import get_db
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.entity.blog import BLOG

from blog.entrypoint.postgresql.models import Blog, User
from blog.model.schemas import BlogSchema


class REPOSTORE(IBLOGREPO):

    def __init__(self, db: Session = Depends(get_db)):
        self.session = db

    def prepare_payload(self, payload: Union[Blog, User]):

        return dict(blog_id=payload.blog_id, title=payload.title, description=payload.description, user_id=payload.user_id)

    def create_blog(self, blog: BlogSchema) -> BLOG:
        blog = Blog(**blog.dict())
        self.session.add(blog)
        self.session.commit()
        return BLOG.from_json(self.prepare_payload(blog))

    def read_blog(self, blog_id: int) -> BLOG:

        blog = self.session.query(Blog).get(blog_id)
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {blog_id} is not available")

        return BLOG.from_json(self.prepare_payload(blog))

    def list_blog(self, user_id: int) -> List[BLOG]:
        blogs = self.session.query(Blog).filter(Blog.user_id == user_id).all()

        if not blogs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {user_id} is not available")

        return [BLOG.from_json(self.prepare_payload(blog)) for blog in blogs]

    def listall_blog(self) -> List[BLOG]:
        blogs = self.session.query(Blog).all()
        print('blogs', blogs)

        if not blogs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"data is not available{blogs}")

        return [BLOG.from_json(self.prepare_payload(blog)) for blog in blogs]

    def update_blog(self, blog: BlogSchema) -> BLOG:

        updated_blog = self.session.query(Blog).update({Blog.title: blog.title, Blog.description: blog.description})
        self.session.commit()
        return BLOG.from_json(self.prepare_payload(updated_blog))

    def delete_blog(self, blog_id: int) -> int:
        blog = self.session.query(Blog).filter(Blog.blog_id == blog_id).delete()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {blog_id} is not available")
        return blog_id


