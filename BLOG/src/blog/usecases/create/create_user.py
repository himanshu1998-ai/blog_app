from blog.repository.interface.user_repo import IUSERREPO
from blog.model.schemas import UserSchema


class CREATEUSERUSECASE:
    def __init__(self, repo: IUSERREPO):
        self.repo = repo

    def execute(self, model: UserSchema):
        data = self.repo.create_user(user=model)
        return data
