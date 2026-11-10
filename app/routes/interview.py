from fastapi import APIRouter

router = APIRouter(prefix="/interview", tags=["interview"])

@router.get("/status")
def interview_status():
    return {"module": "interview", "status": "active"}