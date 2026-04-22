from fastapi import APIRouter
from app.modules.osint_engine import full_scan
from app.modules.ai_summary import generate_summary

router = APIRouter()

@router.get("/summary/{target}")
async def summary(target: str):
    data = await full_scan(target)
    return {
        "target": target,
        "summary": generate_summary(data)
    }