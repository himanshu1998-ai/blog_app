from blog.repository.interface.user_repo import IUSERREPO
from fastapi.security import OAuth2PasswordRequestForm


class LOGINUSERUSECASE:
    def __init__(self, repo: IUSERREPO):
        self.repo = repo

    def execute(self, formdata: OAuth2PasswordRequestForm):
        data = self.repo.login_user(request=formdata)
        return data
