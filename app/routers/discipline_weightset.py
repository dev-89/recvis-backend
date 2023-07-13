from fastapi import APIRouter

router = APIRouter(prefix="/disciplines", tags=["Discipline Weightset"])


@router.post("/add/")
async def add_discipline_weightset():
    return {"username": "fakecurrentuser"}


@router.get("/list")
async def get_weightsets():
    return {"username": "fakecurrentuser"}


@router.get("/<weightset_id>")
async def get_weightset():
    return {"username": "fakecurrentuser"}


@router.patch("/update")
async def update_weightset():
    return {"username": "fakecurrentuser"}


@router.delete("/remove")
async def delete_weightset():
    return {"username": "fakecurrentuser"}
