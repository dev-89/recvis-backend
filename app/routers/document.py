from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["Document"])


@router.get("/list-files/")
async def get_documents():
    return {"username": "fakecurrentuser"}


@router.post("/upload-files")
async def upload_document():
    return {"username": "fakecurrentuser"}


@router.get("/result")
async def get_document_result():
    return {"username": "fakecurrentuser"}
