from blog.repository.interface.user_repo import IUSERREPO
from blog.entity.user import USER


class GETUSERUSECASE:
    def __init__(self, repo: IUSERREPO):
        self.repo = repo

    def execute(self, user_id: int):
        data = self.repo.get_user(user_id=user_id)
        if isinstance(data, USER):
            new_data = {"name": data.name, "email": data.email}
            return new_data
        return data
