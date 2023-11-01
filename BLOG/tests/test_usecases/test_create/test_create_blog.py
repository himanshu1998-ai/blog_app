from pytest_mock import MockerFixture
from unittest.mock import Mock
from blog.entity.blog import BLOG
from blog.usecases.create.create_blog import CREATEBLOGUSECASE
from blog.repository.interface.blog_repo import IBLOGREPO
from blog.model.schemas import BlogSchema


class TestCreateBLOGUseCase:

    def test_orchestrate(self, mocker: MockerFixture):
        self._mocker = mocker
        self.perform_create()

    def _mock_iblog_repo(self):
        return Mock(spec=IBLOGREPO)

    def perform_create(self):
        repo = self._mock_iblog_repo()

        blog = BLOG(blog_id=1, user_id=1, title="test_create_blog", description="testing create blog")
        blog_schema = BlogSchema(user_id=1, title="test_create_blog", description="testing create blog")
        self._mocker.patch.object(
            target=repo,
            attribute="create_blog",
            return_value=blog
        )
        use_case = CREATEBLOGUSECASE(repo)

        result = use_case.execute(model=blog_schema)
        assert blog.blog_id == result.blog_id
        assert blog.user_id == result.user_id
        assert blog.title == result.title
        assert blog.description == result.description
        repo.create_blog.assert_called_once()
