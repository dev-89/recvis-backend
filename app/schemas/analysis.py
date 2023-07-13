from pydantic import BaseModel


class AnalysisBase(BaseModel):
    folderId: str
    filderId: str
