from blog.model.schemas import BlogSchema
from blog.repository.interface.blog_repo import IBLOGREPO
from fastapi import HTTPException


class UPDATEBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, data_to_update: BlogSchema, blog_id: int):
        blog = self.repo.read_blog(blog_id=blog_id)
        if isinstance(blog, HTTPException):
            return blog
        if blog:
            data = self.repo.update_blog(data_to_update, blog_id=blog_id)
            return data
