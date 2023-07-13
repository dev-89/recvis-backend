from fastapi import APIRouter

router = APIRouter(prefix="/folders", tags=["Folders"])


@router.post("/")
async def create_folder():
    return {"username": "fakecurrentuser"}


@router.get("/")
async def get_folders():
    return {"username": "fakecurrentuser"}


@router.delete("/{folder_id}")
async def delete_folder(folder_id: str):
    return {"username": "fakecurrentuser"}
