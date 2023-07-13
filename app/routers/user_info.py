from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User Information"])


@router.get("/")
async def get_discipline():
    return {"username": "fakecurrentuser"}


@router.get("/{user_id}")
async def get_discpline_by_id():
    return {"username": "fakecurrentuser"}
