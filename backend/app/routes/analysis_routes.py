from fastapi import APIRouter, HTTPException
from app.services.drug_analysis import run_analysis

router = APIRouter()

@router.post("")
async def analyze(payload: dict):

    try:
        file_info = payload.get("fileInfo")
        drugs = payload.get("drugs")

        if not file_info or not drugs:
            raise HTTPException(status_code=400, detail="Invalid payload")

        result = await run_analysis(file_info, drugs)
        return result

    except Exception as e:
        print("🔥 ANALYSIS ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
