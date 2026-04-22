from fastapi import APIRouter
from app.modules.ip_osint import get_ip_info

router = APIRouter()

@router.get("/ip/{ip}")
async def ip_lookup(ip: str):
    return await get_ip_info(ip)