from fastapi import APIRouter
from app.modules.username_osint import scan_username

router = APIRouter()

@router.get("/username/{username}")
async def username_lookup(username: str):
    return await scan_username(username)