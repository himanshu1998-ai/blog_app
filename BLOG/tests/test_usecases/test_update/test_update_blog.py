from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.blog import BLOG
from blog.usecases.update.update_blog import UPDATEBLOGUSECASE
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.exception.exception import not_found
from fastapi import HTTPException
from blog.model.schemas import BlogSchema


class TestReadBLOGUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_read()
        self.perform_read_error()

    def _mock_iblog_repo(self):
        return Mock(spec=IBLOGREPO)

    def perform_read(self):
        correct_blog_id = 6
        repo = self._mock_iblog_repo()
        blog = BLOG(blog_id=6, user_id=1, title="test_create_blog", description="testing create blog")
        data_to_update = BlogSchema(user_id=6, title="test", description="test")
        self._mocker.patch.object(
            target=repo,
            attribute="read_blog",
            return_value=blog
        )
        self._mocker.patch.object(
            target=repo,
            attribute="update_blog",
            return_value=f"Blog updated successfully with data=({data_to_update})"
        )
        use_case = UPDATEBLOGUSECASE(repo)

        result = use_case.execute(blog_id=correct_blog_id, data_to_update=data_to_update)
        assert result is not None
        assert data_to_update.title in result
        assert data_to_update.description in result
        repo.read_blog.assert_called_once()
        repo.update_blog.assert_called_once()

    def perform_read_error(self):
        incorrect_blog_id = 10000000000
        repo = self._mock_iblog_repo()
        no_data = not_found(detail=f"Blog with the id {incorrect_blog_id} is not available")
        data_to_update = BlogSchema(user_id=6, title="test", description="test")
        self._mocker.patch.object(
            target=repo,
            attribute="read_blog",
            return_value=no_data
        )
        use_case = UPDATEBLOGUSECASE(repo)

        result = use_case.execute(blog_id=incorrect_blog_id, data_to_update=data_to_update)
        assert result.status_code == 404
        assert type(result) == HTTPException
        assert result.detail == f"Blog with the id {incorrect_blog_id} is not available"
        repo.read_blog.assert_called_once()

