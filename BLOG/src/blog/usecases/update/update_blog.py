from blog.repository.interface.blog_repo import IBLOGREPO


class UPDATEBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, blog_id: int):
        blog = self.repo.read_blog(blog_id=blog_id)
        data = self.repo.update_blog(blog)
        return data
