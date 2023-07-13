from beanie import Document


class CollectedDocuments(Document):
    user_mail = str
    documentId = int
    title = str
    authorList = list[str]


class CollectedDocumentOrder(Document):
    user_mail = str
    order = list[int]
