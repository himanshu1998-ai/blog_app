from blog.repository.interface.blog_repo import IBLOGREPO


class DELETEBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, blog_id: int):
        data = self.repo.delete_blog(blog_id=blog_id)
        return data
