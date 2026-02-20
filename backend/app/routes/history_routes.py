from fastapi import APIRouter
from app.core.database import db

router = APIRouter()

@router.get("")
async def get_history():
    records = []
    async for doc in db.history.find().sort("date", -1):
        doc["_id"] = str(doc["_id"])
        records.append(doc)
    return records