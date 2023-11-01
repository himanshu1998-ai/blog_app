from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.user import USER
from blog.hashing.hash import bcrypt
from blog.usecases.create.create_user import CREATEUSERUSECASE
from blog.repository.interface.user_repo import IUSERREPO
from blog.model.schemas import UserSchema


class TestCreateUSERUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_create()

    def _mock_iblog_repo(self):
        return Mock(spec=IUSERREPO)

    def perform_create(self):
        repo = self._mock_iblog_repo()

        user = USER(user_id=1, name="test_name", email="test@mail.com", password=bcrypt("1234"))
        user_schema = UserSchema(name="test_name", email="test@mail.com", password="1234")
        self._mocker.patch.object(
            target=repo,
            attribute="create_user",
            return_value=user
        )
        use_case = CREATEUSERUSECASE(repo)

        result = use_case.execute(model=user_schema)
        assert user.name == result.name
        assert user.email == result.email
        assert user.user_id is not None
        assert result.password is not None
        assert user_schema.password != result.password

        repo.create_user.assert_called_once()
