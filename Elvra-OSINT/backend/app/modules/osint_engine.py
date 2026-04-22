from app.modules.ip_osint import get_ip_info
from app.modules.subdomain_osint import scan_subdomains
from app.modules.username_osint import scan_username
from app.modules.risk_score import calculate_risk
from app.modules.web_sources import get_public_sources

import asyncio

async def full_scan(target: str):
    ip_task = get_ip_info(target)
    sub_task = scan_subdomains(target)
    user_task = scan_username(target)

    ip_data, sub_data, user_data = await asyncio.gather(
        ip_task, sub_task, user_task, return_exceptions=True
    )

    risk = calculate_risk(ip_data if not isinstance(ip_data, Exception) else None)
    sources = get_public_sources(target)

    return {
        "target": target,
        "ip": ip_data if not isinstance(ip_data, Exception) else None,
        "subdomains": sub_data if not isinstance(sub_data, Exception) else None,
        "username": user_data if not isinstance(user_data, Exception) else None,
        "risk": risk,
        "sources": sources
    }