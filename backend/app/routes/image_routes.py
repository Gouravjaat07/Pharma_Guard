from fastapi import APIRouter
from app.services.image_service import scan_medicine

router = APIRouter()

@router.post("/scan")
async def scan(payload: dict):
    return await scan_medicine(payload["base64"], payload["mediaType"]) 