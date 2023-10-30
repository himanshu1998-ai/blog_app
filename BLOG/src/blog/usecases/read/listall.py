from blog.repository.interface.blog_repo import IBLOGREPO


class LISTBLOGUSECASE:
    def __init__(self, repo: IBLOGREPO):
        self.repo = repo

    def execute(self, user_id: int):
        data = self.repo.list_blog(user_id=user_id)
        return data
