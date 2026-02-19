from fastapi import APIRouter, UploadFile, File
from app.services.vcf_parser import parse_vcf

router = APIRouter()

@router.post("/upload")
async def upload_vcf(file: UploadFile = File(...)):
    content = await file.read()
    parsed = await parse_vcf(content, file.filename)
    return parsed