from beanie import Document


class Folder(Document):
    user_mail: str
    folder_name: str
    file_count: int
    files: list[str]
