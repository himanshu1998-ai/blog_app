class USER:
    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_json(cls, json):
        return cls(**json)

    def to_json(self):
        return self.__dict__.copy()
