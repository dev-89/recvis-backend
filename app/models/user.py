from beanie import Document


class User(Document):
    email: str
    password: str
    discipline: str
