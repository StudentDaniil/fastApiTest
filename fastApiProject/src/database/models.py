from pydantic import BaseModel, Field


class FromF(BaseModel):
    is_bot: bool
    first_name: str
    last_name: str = None
    username: str = None

    def to_dict(self):
        return {
            'is_bot': self.is_bot,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
        }


class Message(BaseModel):
    text: str
    from_f: FromF = None
