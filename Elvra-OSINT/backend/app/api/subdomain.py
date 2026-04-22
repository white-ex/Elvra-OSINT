from fastapi import APIRouter
from app.modules.subdomain_osint import scan_subdomains

router = APIRouter()

@router.get("/subdomains/{domain}")
async def subdomain_scan(domain: str):
    return await scan_subdomains(domain)