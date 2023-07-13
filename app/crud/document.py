import random

from fastapi import HTTPException

from app.crud.folder import folder_controller
from app.models.document import UserDocument


class CRUDDocument:
    def __init__(self) -> None:
        self.model = UserDocument

    async def get_document(self, document_id: str) -> UserDocument:
        user_doc = await self.model.get(document_id)
        if not user_doc:
            raise HTTPException(
                status_code=404,
                detail=f"Could not find document with ID {document_id}.",
            )
        return user_doc

    async def delete_document(self, document_id: str) -> UserDocument:
        user_doc = await self.get_document(document_id)
        await user_doc.delete()
        return user_doc

    def create_document(
        self, user_mail: str, folder_id: str, file_name: str
    ) -> UserDocument:
        user_doc = self.model(
            user_mail=user_mail,
            hyplag_id=random.randint(1, 9999),
            folder_id=folder_id,
            fileName=file_name,
        )
        saved_doc = await user_doc.save()
        folder_controller.add_document_to_folder(user_mail, folder_id, saved_doc.id)
        return saved_doc

    async def update_document(
        self,
        document_id: str,
        analysis_id: str,
        is_analysis_in_progress: bool,
    ) -> UserDocument:
        user_doc = await self.get_document(document_id)
        user_doc.isAnalysisInProgress = is_analysis_in_progress
        user_doc.analysisID = analysis_id
        await user_doc.save()
        return user_doc

    async def get_documents_by_folder(
        self, user_mail: str, folder_id: str
    ) -> list[UserDocument]:
        return await self.model.find(user_mail=user_mail, folder_id=folder_id).to_list()
