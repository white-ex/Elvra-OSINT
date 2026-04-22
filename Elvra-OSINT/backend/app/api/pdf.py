from fastapi import APIRouter
from app.modules.pdf_report import generate_pdf

router = APIRouter()

@router.get("/pdf/{target}")
async def pdf(target: str):
    file = await generate_pdf(target)
    return {"file": file}