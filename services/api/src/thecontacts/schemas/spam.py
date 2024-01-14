from pydantic import BaseModel

class Spam(BaseModel):
    name: str
    phone: str
    email: str = None
    owner: str