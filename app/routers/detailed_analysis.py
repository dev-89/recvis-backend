from fastapi import APIRouter

router = APIRouter(prefix="/detailed-analysis", tags=["Detailed Analysis"])


@router.post("/compare/")
async def read_users():
    return {"username": "fakecurrentuser"}


@router.post("/document-data")
async def user_document_data():
    return {"username": "fakecurrentuser"}


@router.post("/document-meta")
async def user_document_meta_data():
    return {"username": "fakecurrentuser"}
