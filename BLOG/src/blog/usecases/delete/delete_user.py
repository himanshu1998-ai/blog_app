from blog.repository.interface.user_repo import IUSERREPO



class DELETEUSERUSECASE:
    def __init__(self, repo: IUSERREPO):
        self.repo = repo

    def execute(self, user_id: int):
        data = self.repo.delete_user(user_id=user_id)
        return data
