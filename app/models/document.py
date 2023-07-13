from beanie import Document


class UserDocument(Document):
    fileName: str = "Nameless"
    hyplag_id = int
    user_mail = str
    folder_id = int
    analysisID: str = None
    isAnalysisInProgress: bool = False
    keywords: list[str] = []
    paper_title: str = ""
    num_recommendations: int = 10
