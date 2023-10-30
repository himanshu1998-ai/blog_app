from blog.repository.interface.blog_repo import IBLOGREPO


class READBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, blog_id: int):
        data = self.repo.read_blog(blog_id=blog_id)
        return data
