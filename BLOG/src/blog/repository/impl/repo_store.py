from typing import Union, List
from sqlalchemy.orm import Session

from fastapi import Depends

from blog.entrypoint.postgresql.database import get_db
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.entity.blog import BLOG

from blog.entrypoint.postgresql.models import Blog, User
from blog.model.schemas import BlogSchema
from blog.exception import exception


class REPOSTORE(IBLOGREPO):

    def __init__(self, db: Session = Depends(get_db)):
        self.session = db

    def prepare_payload(self, payload: Union[Blog, User]):

        return dict(blog_id=payload.blog_id, title=payload.title, description=payload.description, user_id=payload.user_id)

    def create_blog(self, blog: BlogSchema) -> Union[BLOG, str]:
        try:
            blog = Blog(**blog.model_dump())
            self.session.add(blog)
            self.session.commit()
            return BLOG.from_json(self.prepare_payload(blog))

        except Exception as e:

            return f"Exception: {e}-- occurred while creating blog with data: {blog}"

    def read_blog(self, blog_id: int) -> Union[BLOG, str]:
        try:

            blog = self.session.query(Blog).get(blog_id)
            if not blog:
                return exception.not_found(detail=f"Blog with the id {blog_id} is not available")

            return BLOG.from_json(self.prepare_payload(blog))
        except Exception as e:
            return f"Exception: {e}-- occurred while fetching blog with blog_id: {blog_id}"

    def list_blog(self, user_id: int) -> Union[List[BLOG], str]:
        try:
            blogs = self.session.query(Blog).filter(Blog.user_id == user_id).all()

            if not blogs:

                return exception.not_found(detail=f"User with the id {user_id} is not available")
            return [BLOG.from_json(self.prepare_payload(blog)) for blog in blogs]

        except Exception as e:
            return f"Exception: {e}-- occurred while fetching list blog with user_id: {user_id}"

    def listall_blog(self) -> Union[List[BLOG], str]:
        try:
            blogs = self.session.query(Blog).all()
            if not blogs:
                return exception.not_found(detail=f"data is not available{blogs}")

            return [BLOG.from_json(self.prepare_payload(blog)) for blog in blogs]
        except Exception as e:
            return f"Exception: {e}-- occurred while fetching list all blog"

    def update_blog(self, blog: BlogSchema, blog_id: int) -> str:
        try:
            self.session.query(Blog).filter(Blog.user_id == blog.user_id, Blog.blog_id == blog_id).update({Blog.title: blog.title, Blog.description: blog.description})
            self.session.commit()
            return f"Blog updated successfully with data=({blog})"
        except Exception as e:
            return f"Exception: {e}-- occurred while updating blog with data: {blog}"

    def delete_blog(self, blog_id: int) -> Union[int, str]:
        try:
            blog = self.session.query(Blog).filter(Blog.blog_id == blog_id).delete()
            if not blog:

                return exception.not_found(detail=f"User with the id {blog_id} is not available")

            return blog_id
        except Exception as e:
            return f"Exception: {e}-- occurred while deleting blog with blog_id: {blog_id}"


