from blog.repository.interface.user_repo import IUSERREPO
from blog.entity.user import USER
from blog.model.schemas import ShowUser


class GETUSERUSECASE:
    def __init__(self, repo: IUSERREPO):
        self.repo = repo

    def execute(self, user_id: int):
        no_data = ShowUser(name="Not Found", email="Not Found")
        data = self.repo.get_user(user_id=user_id)
        if isinstance(data, USER):
            return data
        return no_data

