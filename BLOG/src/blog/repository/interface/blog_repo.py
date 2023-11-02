from typing import List
from abc import ABC, abstractmethod
from blog.entity.blog import BLOG
from blog.model.schemas import BlogSchema


class IBLOGREPO(ABC):

    @abstractmethod
    def create_blog(self, blog: BlogSchema) -> BLOG:
        pass

    @abstractmethod
    def read_blog(self, blog_id: int) -> BLOG:
        pass

    @abstractmethod
    def list_blog(self, user_id: int) -> List[BLOG]:
        pass

    @abstractmethod
    def listall_blog(self) -> List[BLOG]:
        pass

    @abstractmethod
    def update_blog(self, blog: BlogSchema, blog_id: int) -> BLOG:
        pass

    @abstractmethod
    def delete_blog(self, blog_id: int) -> int:
        pass



