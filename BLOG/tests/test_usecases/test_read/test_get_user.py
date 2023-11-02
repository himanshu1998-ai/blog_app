from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.user import USER
from blog.hashing.hash import bcrypt
from blog.model.schemas import ShowUser
from blog.usecases.read.get_user import GETUSERUSECASE
from blog.repository.interface.user_repo import IUSERREPO
from blog.exception.exception import not_found


class TestCreateUSERUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_read()
        self.perform_read_error()

    def _mock_iuser_repo(self):
        return Mock(spec=IUSERREPO)

    def perform_read(self):
        correct_user_id = 1
        repo = self._mock_iuser_repo()
        user = USER(user_id=1, name="test_name", email="test@mail.com", password=bcrypt("1234"))

        self._mocker.patch.object(
            target=repo,
            attribute="get_user",
            return_value=user
        )
        use_case = GETUSERUSECASE(repo)

        result = use_case.execute(user_id=correct_user_id)
        assert isinstance(result, ShowUser)
        assert user.name == result.name
        assert user.email == result.email

        repo.get_user.assert_called_once()

    def perform_read_error(self):
        incorrect_user_id = 100000000000000000
        repo = self._mock_iuser_repo()
        no_user = not_found(detail=f"User with the id {incorrect_user_id} is not available")
        self._mocker.patch.object(
            target=repo,
            attribute="get_user",
            return_value=no_user
        )
        use_case = GETUSERUSECASE(repo)
        result = use_case.execute(user_id=incorrect_user_id)

        assert isinstance(result, ShowUser)
        assert result.name == "Not Found"
        assert result.email == "Not Found"

        repo.get_user.assert_called_once()
