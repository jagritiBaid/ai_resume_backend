from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/status")
def chat_status():
    return {"module": "chat", "status": "active"}