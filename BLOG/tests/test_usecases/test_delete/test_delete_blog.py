from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.usecases.delete.delete_blog import DELETEBLOGUSECASE
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.exception.exception import not_found
from fastapi import HTTPException


class TestReadBLOGUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_delete()
        self.perform_delete_error()

    def _mock_iblog_repo(self):
        return Mock(spec=IBLOGREPO)

    def perform_delete(self):
        correct_blog_id = 6
        repo = self._mock_iblog_repo()
        self._mocker.patch.object(
            target=repo,
            attribute="delete_blog",
            return_value=correct_blog_id
        )

        use_case = DELETEBLOGUSECASE(repo)

        result = use_case.execute(blog_id=correct_blog_id)
        assert result is not None
        assert result == correct_blog_id
        repo.delete_blog.assert_called_once()

    def perform_delete_error(self):
        incorrect_blog_id = 10000000000
        repo = self._mock_iblog_repo()
        no_data = not_found(detail=f"User with the id {incorrect_blog_id} is not available")
        self._mocker.patch.object(
            target=repo,
            attribute="delete_blog",
            return_value=no_data
        )
        use_case = DELETEBLOGUSECASE(repo)

        result = use_case.execute(blog_id=incorrect_blog_id)
        assert result.status_code == 404
        assert type(result) == HTTPException
        assert result.detail == f"Blog with the id {incorrect_blog_id} is not available"
        repo.delete_blog.assert_called_once()

