from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class UserInDb(User):
    hashed_password: str
    