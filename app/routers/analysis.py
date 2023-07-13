from fastapi import APIRouter

router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.post("/")
async def create_analysis():
    return {"username": "fakecurrentuser"}


@router.get("/{analysis_id}/status")
async def get_analysis_status():
    return {"username": "fakecurrentuser"}


@router.get("/{analysis_id}")
async def get_analysis():
    return {"username": "fakecurrentuser"}
