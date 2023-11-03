from fastapi import HTTPException
from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.user import USER
from blog.exception.exception import not_found
from blog.hashing.hash import bcrypt
from blog.usecases.delete.delete_user import DELETEUSERUSECASE
from blog.repository.interface.user_repo import IUSERREPO
from blog.model.schemas import UserSchema


class TestCreateUSERUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_delete()
        self.perform_delete_error()

    def _mock_iuser_repo(self):
        return Mock(spec=IUSERREPO)

    def perform_delete(self):
        correct_user_id = 1
        repo = self._mock_iuser_repo()

        self._mocker.patch.object(
            target=repo,
            attribute="delete_user",
            return_value=correct_user_id
        )
        use_case = DELETEUSERUSECASE(repo)

        result = use_case.execute(user_id=correct_user_id)
        assert result is not None
        assert result == correct_user_id
        repo.delete_user.assert_called_once()

    def perform_delete_error(self):
        incorrect_user_id = 100000000
        repo = self._mock_iuser_repo()
        no_data = not_found(detail=f"User with the id {incorrect_user_id} is not available")
        self._mocker.patch.object(
            target=repo,
            attribute="delete_user",
            return_value=no_data
        )
        use_case = DELETEUSERUSECASE(repo)

        result = use_case.execute(user_id=incorrect_user_id)
        assert result is not None
        assert result.status_code == 404
        assert type(result) == HTTPException
        assert result.detail == f"User with the id {incorrect_user_id} is not available"
        repo.delete_user.assert_called_once()
