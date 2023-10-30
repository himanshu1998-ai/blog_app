from blog.repository.interface.blog_repo import IBLOGREPO


class LISTALLBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self):
        data = self.repo.listall_blog()
        return data