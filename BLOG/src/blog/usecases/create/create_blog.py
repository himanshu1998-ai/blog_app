from blog.repository.interface.blog_repo import IBLOGREPO
from blog.model.schemas import BlogSchema


class CREATEBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, model: BlogSchema):
        data = self.repo.create_blog(blog=model)
        return data
