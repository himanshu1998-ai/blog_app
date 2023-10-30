class BLOG:
    def __init__(self, blog_id: int, title: str, description: str, user_id: int):
        self.blog_id = blog_id
        self.title = title
        self.description = description
        self.user_id = user_id

    @property
    def get_user_id(self):
        return self.user_id

    @classmethod
    def from_json(cls, json):
        return cls(**json)

    def to_json(self):
        return self.__dict__.copy()

