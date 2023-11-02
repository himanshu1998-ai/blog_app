from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.blog import BLOG
from blog.usecases.read.read_blog import READBLOGUSECASE
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.exception.exception import not_found
from fastapi import HTTPException


class TestReadBLOGUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_read()
        self.perform_read_error()

    def _mock_iblog_repo(self):
        return Mock(spec=IBLOGREPO)

    def perform_read(self):
        correct_blog_id = 1
        repo = self._mock_iblog_repo()
        blog = BLOG(blog_id=1, user_id=1, title="test_create_blog", description="testing create blog")

        self._mocker.patch.object(
            target=repo,
            attribute="read_blog",
            return_value=blog
        )
        use_case = READBLOGUSECASE(repo)

        result = use_case.execute(blog_id=correct_blog_id)
        assert correct_blog_id == result.blog_id
        assert blog.user_id == result.user_id
        assert blog.title == result.title
        assert blog.description == result.description

        repo.read_blog.assert_called_once()

    def perform_read_error(self):
        incorrect_blog_id = 10000000000
        repo = self._mock_iblog_repo()
        no_data = not_found(detail=f"Blog with the id {incorrect_blog_id} is not available")
        self._mocker.patch.object(
            target=repo,
            attribute="read_blog",
            return_value=no_data
        )
        use_case = READBLOGUSECASE(repo)

        result = use_case.execute(blog_id=incorrect_blog_id)
        assert result.status_code == 404
        assert type(result) == HTTPException
        assert result.detail == f"Blog with the id {incorrect_blog_id} is not available"
        repo.read_blog.assert_called_once()
