from fastapi import APIRouter
from app.modules.osint_engine import full_scan

router = APIRouter()

@router.get("/scan/{target}")
async def scan(target: str):
    return await full_scan(target)