from fastapi import APIRouter
from app.modules.risk_score import calculate_risk
from app.modules.ip_osint import get_ip_info

router = APIRouter()

@router.get("/risk/{ip}")
async def risk_test(ip: str):
    ip_data = await get_ip_info(ip)
    return calculate_risk(ip_data)