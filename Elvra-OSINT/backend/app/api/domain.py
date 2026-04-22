from fastapi import APIRouter
from app.modules.domain_osint import get_domain_info

router = APIRouter()

@router.get("/domain/{domain}")
async def domain_lookup(domain: str):
    return await get_domain_info(domain)