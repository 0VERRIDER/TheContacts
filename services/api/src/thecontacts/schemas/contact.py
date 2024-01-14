from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    phone: str
    email: str = None
    owner: str

class ContactInDB(Contact):
    id: str