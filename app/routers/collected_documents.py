from fastapi import APIRouter

router = APIRouter(prefix="/collected-docs", tags=["Collected Documents"])


@router.post("/append/")
async def read_users():
    return {"username": "fakecurrentuser"}


@router.get("/")
async def get_collected_documents():
    return {"username": "fakecurrentuser"}


@router.delete("/")
async def delete_collected_document():
    return {"username": "fakecurrentuser"}


@router.patch("/set-order")
async def set_collected_document_order():
    return {"username": "fakecurrentuser"}
