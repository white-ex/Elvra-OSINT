import httpx
import asyncio

SUBDOMAINS = [
    "www",
    "mail",
    "ftp",
    "admin",
    "api",
    "dev",
    "test"
]

async def check_subdomain(domain, sub):
    url = f"http://{sub}.{domain}"

    try:
        async with httpx.AsyncClient(timeout=3) as client:
            r = await client.get(url)
            return url
    except:
        return None


async def scan_subdomains(domain: str):
    tasks = []

    for sub in SUBDOMAINS:
        tasks.append(check_subdomain(domain, sub))

    results = await asyncio.gather(*tasks)

    return {
        "domain": domain,
        "subdomains": [r for r in results if r]
    }