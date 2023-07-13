from fastapi import HTTPException

from app.models.folder import Folder


class CRUDFolder:
    def __init__(self) -> None:
        self.model = Folder

    async def delete_folder(self, folder_id: str, user_id: str) -> Folder | None:
        folder = await self.model.find_one(user_mail=user_id, folder_name=folder_id)
        if not folder:
            return None
        await folder.delete()
        return folder

    async def get_folders(self, user_mail: str) -> list[Folder]:
        return await self.model.find_all(user_mail=user_mail)

    async def create_folder(self, folder_name: str, user_mail: str) -> Folder:
        folder = await self.model.find_one(user_mail=user_mail, folder_name=folder_name)
        if folder:
            raise HTTPException(
                status_code=403,
                detail=f"Folder {folder_name} for user {user_mail} already exists.",
            )
        folder = self.model(
            user_mail=user_mail, folder_name=folder_name, file_count=0, files=[]
        )
        await folder.insert()
        return folder

    async def add_document_to_folder(
        self, user_mail: str, folder_name: str, document_id: str
    ) -> Folder:
        folder = await self.model.find_one(folder_name=folder_name, user_mail=user_mail)
        if not folder:
            raise HTTPException(
                status_code=404,
                detail=f"Could not find folder {folder_name} for user {user_mail}.",
            )
        folder.file_count = folder.file_count + 1
        folder.files.append(document_id)
        await folder.save()
        return folder


folder_controller = CRUDFolder()
