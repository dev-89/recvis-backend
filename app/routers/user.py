from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register/")
async def read_users():
    return {"username": "fakecurrentuser"}


@router.post("/login")
async def read_user_me():
    return {"username": "fakecurrentuser"}
