from pydantic import BaseModel


class FolderBase(BaseModel):
    folderName: str


class Folder(FolderBase):
    _id: str
    fileCount: int
