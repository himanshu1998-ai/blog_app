from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.blog import BLOG
from blog.usecases.read.listall import LISTBLOGUSECASE
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.exception.exception import not_found
from fastapi import HTTPException


class TestListBLOGUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_read()
        self.perform_read_error()

    def _mock_iblog_repo(self):
        return Mock(spec=IBLOGREPO)

    def perform_read(self):
        correct_user_id = 1
        repo = self._mock_iblog_repo()
        blog1 = BLOG(blog_id=1, user_id=1, title="test_list_blog", description="testing list blog")
        blog2 = BLOG(blog_id=2, user_id=1, title="test_list_blog", description="testing list blog")
        list_of_blog = [blog1, blog2]
        self._mocker.patch.object(
            target=repo,
            attribute="list_blog",
            return_value=list_of_blog
        )
        use_case = LISTBLOGUSECASE(repo)

        result = use_case.execute(user_id=correct_user_id)
        assert type(result) == list

        repo.list_blog.assert_called_once()

    def perform_read_error(self):
        incorrect_user_id = 10000000000
        repo = self._mock_iblog_repo()
        no_data = not_found(detail=f"User with the id {incorrect_user_id} is not available")
        self._mocker.patch.object(
            target=repo,
            attribute="list_blog",
            return_value=no_data
        )
        use_case = LISTBLOGUSECASE(repo)

        result = use_case.execute(user_id=incorrect_user_id)
        assert result.status_code == 404
        assert type(result) == HTTPException
        assert result.detail == f"User with the id {incorrect_user_id} is not available"
        repo.list_blog.assert_called_once()
